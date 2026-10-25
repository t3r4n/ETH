# Clasificación temprana de ataques MEV tipo sándwich con aprendizaje por refuerzo

Tesis de pregrado en Ciencia de Datos, Universidad Externado de Colombia.
Autora: Sharik Garzón Terán. Tutor: Julián Sánchez.

## Pregunta de investigación
¿Qué desempeño presenta un modelo de aprendizaje por refuerzo, comparado con un
modelo determinista tradicional, en la detección temprana de ataques MEV tipo
sándwich en Ethereum?

## Alcance
Evaluación en un entorno de simulación construido a partir de datos de la mempool.
No incluye despliegue en producción ni evaluación sobre mempool privada
(línea de trabajo futuro).

## Estado
| Componente | Ubicación | Estado |
|---|---|---|
| Recolección de mempool | `src/recolector.py` | v2 escrita, falta probarla con Alchemy |
| EDA de la muestra piloto | `EDA/` | En curso |
| Protocolo de comparación | `docs/protocolo_comparacion.md` | Plantilla, decisiones abiertas |
| Entorno MempoolEnv | `Agente_RL/` | Especificación, sin código |
| Baseline determinista | `baselines/` | Sin implementar |

## Estructura
```
docs/        protocolo, bitácora, reportes de avance, recursos de investigación
data/        muestras pequeñas (los datasets grandes no se suben a Git)
src/         recolector y utilidades
baselines/   modelos deterministas de referencia
Agente_RL/   entorno y agente
EDA/         análisis exploratorio
```

## Cómo reproducir la recolección
```bash
pip install -r requirements.txt
export ALCHEMY_WS="wss://eth-mainnet.g.alchemy.com/v2/<TU_CLAVE>"   # nunca subir la clave
python src/recolector.py
```
Variables opcionales: `OUT_DIR` (por defecto `data/raw`), `LOG_DIR` (`logs`),
`DURATION_SECONDS` (0 = sin límite).

## Seguimiento
Ver `docs/bitacora.md`. Los reportes de avance están en `docs/`.

## Licencia
MIT
