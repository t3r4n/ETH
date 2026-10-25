"""Recolector de mempool vía Alchemy WebSocket (v2).

Mejoras sobre la v1: reconexión con espera creciente, campo input completo,
rotación horaria de archivos, log y cierre limpio con Ctrl+C.
La clave se lee de la variable de entorno ALCHEMY_WS (nunca va en el código).

Variables opcionales:
  OUT_DIR           carpeta de salida (por defecto data/raw)
  LOG_DIR           carpeta de logs (por defecto logs)
  DURATION_SECONDS  duración máxima de la corrida; 0 = sin límite
"""
import asyncio
import csv
import json
import logging
import os
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import websockets

CAMPOS = ["recv_ts_utc", "hash", "from", "to", "value", "gas", "gasPrice",
          "maxFeePerGas", "maxPriorityFeePerGas", "nonce", "type", "input"]

SUBSCRIBE = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "eth_subscribe",
    "params": ["alchemy_pendingTransactions", {"hashesOnly": False}],
}

log = logging.getLogger("recolector")


def parse_message(raw):
    """Devuelve un dict con CAMPOS, o None si el mensaje no es una transacción."""
    try:
        msg = json.loads(raw)
    except (TypeError, ValueError):
        return None
    tx = (msg.get("params") or {}).get("result")
    if not isinstance(tx, dict) or "hash" not in tx:
        return None
    row = {k: tx.get(k) for k in CAMPOS if k != "recv_ts_utc"}
    row["recv_ts_utc"] = datetime.now(timezone.utc).isoformat()
    return row


class RotatingCsv:
    """Escribe filas en un CSV por hora (UTC), con encabezado en cada archivo nuevo."""

    def __init__(self, out_dir):
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.hour = None
        self.fh = None
        self.writer = None
        self.rows = 0

    def write(self, row):
        hour = row["recv_ts_utc"][:13]  # AAAA-MM-DDTHH
        if hour != self.hour:
            self.close()
            name = "mempool_" + hour.replace("-", "").replace("T", "_") + ".csv"
            path = self.out_dir / name
            is_new = not path.exists()
            self.fh = open(path, "a", newline="", encoding="utf-8")
            self.writer = csv.DictWriter(self.fh, fieldnames=CAMPOS)
            if is_new:
                self.writer.writeheader()
            self.hour = hour
            log.info("Escribiendo en %s", path)
        self.writer.writerow(row)
        self.rows += 1
        if self.rows % 500 == 0:
            self.fh.flush()

    def close(self):
        if self.fh:
            self.fh.close()
            self.fh = None


def setup_logging():
    log_dir = Path(os.environ.get("LOG_DIR", "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    log.setLevel(logging.INFO)
    for handler in (logging.StreamHandler(), logging.FileHandler(log_dir / "recolector.log")):
        handler.setFormatter(fmt)
        log.addHandler(handler)


async def run():
    url = os.environ.get("ALCHEMY_WS")
    if not url:
        sys.exit("Falta la variable de entorno ALCHEMY_WS (URL wss:// con tu clave).")
    duration = int(os.environ.get("DURATION_SECONDS", "0"))
    deadline = time.monotonic() + duration if duration > 0 else None
    sink = RotatingCsv(os.environ.get("OUT_DIR", "data/raw"))
    backoff, total, in_window, window_start = 1, 0, 0, time.monotonic()
    try:
        while deadline is None or time.monotonic() < deadline:
            try:
                async with websockets.connect(url, ping_interval=20, ping_timeout=20,
                                              max_size=None) as ws:
                    await ws.send(json.dumps(SUBSCRIBE))
                    log.info("Conectado y suscrito")
                    backoff = 1
                    async for raw in ws:
                        row = parse_message(raw)
                        if row:
                            sink.write(row)
                            total += 1
                            in_window += 1
                        now = time.monotonic()
                        if now - window_start >= 60:
                            log.info("Último minuto: %d tx | total: %d", in_window, total)
                            in_window, window_start = 0, now
                        if deadline is not None and now >= deadline:
                            return
            except (websockets.ConnectionClosed, OSError, asyncio.TimeoutError) as exc:
                log.warning("Conexión perdida (%s). Reintentando en %ds", exc, backoff)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 60)
    finally:
        sink.close()
        log.info("Cerrado. Transacciones guardadas en esta corrida: %d", total)


def main():
    setup_logging()
    loop = asyncio.new_event_loop()
    task = loop.create_task(run())
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, task.cancel)
        except NotImplementedError:  # Windows
            pass
    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        log.info("Detenido por el usuario")
    finally:
        loop.close()


if __name__ == "__main__":
    main()
