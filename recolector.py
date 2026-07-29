import asyncio, websockets, json, csv, os
from datetime import datetime

ALCHEMY_WS = os.environ["ALCHEMY_WS"]  
CAMPOS = ["timestamp","hash","from","to","value","gas","maxFeePerGas",
          "maxPriorityFeePerGas","input"]

async def recolectar(duracion_segundos=1800):
    with open("mempool_sample.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        async with websockets.connect(ALCHEMY_WS) as ws:
            sub = {"jsonrpc":"2.0","id":1,"method":"eth_subscribe",
                   "params":["alchemy_pendingTransactions", {"hashesOnly": False}]}
            await ws.send(json.dumps(sub))
            await ws.recv()
            inicio = asyncio.get_event_loop().time()
            while asyncio.get_event_loop().time() - inicio < duracion_segundos:
                msg = json.loads(await ws.recv())
                tx = msg.get("params", {}).get("result", {})
                if tx:
                    writer.writerow({
                        "timestamp": datetime.utcnow().isoformat(),
                        "hash": tx.get("hash"),
                        "from": tx.get("from"),
                        "to": tx.get("to"),
                        "value": tx.get("value"),
                        "gas": tx.get("gas"),
                        "maxFeePerGas": tx.get("maxFeePerGas"),
                        "maxPriorityFeePerGas": tx.get("maxPriorityFeePerGas"),
                        "input": tx.get("input", "")[:20],
                    })

asyncio.run(recolectar(1800))