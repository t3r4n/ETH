# Protocolo de comparación RL vs. modelo determinista

Estado: BORRADOR. Los puntos marcados TODO son decisiones abiertas para discutir con el tutor.

## 1. Objetivo
Comparar el desempeño de un agente de RL contra un baseline determinista en la
detección de ataques sándwich, sobre los mismos datos y con la misma verdad terreno.

## 2. Datos
- Fuente: mempool vía proveedor RPC (Alchemy), recolección continua.
- Ventana de recolección: TODO (propuesta a discutir: 7 a 14 días continuos).
- Partición: cronológica (entrenamiento, validación, prueba), sin mezclar tiempos.
  Proporciones: TODO.

## 3. Qué ve cada modelo y cuándo
| Modelo | Información disponible | Momento de decisión |
|---|---|---|
| Agente RL | Transacciones pendientes (ventana H=10, K=5) | Antes de la confirmación |
| Baseline determinista | TODO (bloque confirmado, logs de eventos) | Después de la confirmación |

Riesgo a documentar: si los baselines solo operan sobre bloques confirmados, la
comparación de exactitud y la de oportunidad miden cosas distintas.
TODO: decidir si se compara (a) exactitud sobre los mismos casos, (b) tiempo de
detección, o ambas, y cómo se interpreta cada una.

## 4. Verdad terreno
- Fuente prevista: EigenPhi.
- TODO: verificar si hay acceso por API o descarga y qué rango de bloques cubre.
- TODO: definir cómo se mapea una transacción pendiente a un ataque confirmado.

## 5. Métricas
Precisión, recall, F1, tiempo de detección respecto a la confirmación en bloque,
tasa de falsos positivos. TODO: pruebas de significancia y número de semillas
de entrenamiento.

## 6. Baselines
- Park et al. (2023), Algoritmo 1 (determinista).
- Li et al. (2024) (detector en Geth). TODO: confirmar si entra.
- TODO: decidir si Bai et al. (2025) se mantiene como referencia en el objetivo 3.

## 7. Amenazas a la validez
- Visibilidad parcial de la mempool (un solo punto de observación).
- Sesgo temporal de la ventana de recolección.
- Etiquetas con errores (los detectores tienen falsos positivos y negativos).
- Deriva del comportamiento de los atacantes.

## 8. Preguntas para el tutor
1.
2.
