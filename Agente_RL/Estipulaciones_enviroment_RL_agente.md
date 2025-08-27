## Diseño del Entorno del Agente de Aprendizaje por Refuerzo

El entorno del agente autónomo está diseñado para modelar la detección de **ataques tipo sándwich** asociados al **Miner Extractable Value (MEV)** en la red Ethereum, utilizando datos provenientes de **Eigenphi**. Este entorno se formaliza dentro del marco de **aprendizaje por refuerzo**, considerando el espacio de estados, acciones, probabilidades de transición, acciones admisibles, función de recompensa y política óptima.  

### Espacio de Estados
El **estado** del sistema en un instante \( t \) se define como un vector que resume la información disponible en el mempool y las características de las transacciones relevantes para MEV. El vector de estado incluye variables tales como: número de ataques tipo sándwich detectados, cantidad de atacantes y víctimas involucradas, volumen total de transacciones, retorno de inversión (ROI) estimado y actividad de bots MEV. Formalmente, un estado se representa como:  

\[
s_t = [\text{Sandwich Count}, \text{Attackers}, \text{Victims}, \text{Volume}, \text{ROI}, \text{Bot Activity}]
\]  

El **espacio de estados** \( S \) puede considerarse discreto o continuo dependiendo de la granularidad elegida para las métricas cuantitativas, y refleja toda la información relevante para la toma de decisiones del agente.  

### Espacio de Acciones
El agente puede ejecutar un conjunto de **acciones discretas** sobre cada transacción o conjunto de transacciones en el mempool. Las acciones disponibles son:  

- \( a_1 \): Clasificar la transacción como ataque tipo sándwich.  
- \( a_2 \): Clasificar la transacción como no ataque.  

El conjunto de acciones se define formalmente como:  

\[
A = \{ a_1, a_2 \}
\]  

Estas acciones permiten al agente decidir sobre la presencia o ausencia de un ataque en cada unidad de análisis.  

### Probabilidades de Transición
Las probabilidades de transición \( P(s_{t+1} | s_t, a_t) \) describen la evolución del estado del sistema tras la ejecución de una acción. Dado que la aparición de ataques y el comportamiento de las transacciones en Ethereum es parcialmente estocástico, se modela como un proceso de **Markov parcial**, donde el siguiente estado depende únicamente del estado actual y la acción tomada. Los cambios en variables como volumen, ROI y actividad de bots combinan patrones históricos determinísticos y fluctuaciones aleatorias, representando la naturaleza compleja y dinámica del entorno MEV.  

### Acciones Admisibles
Las acciones admisibles están restringidas a decisiones consistentes sobre cada transacción:  
- Cada transacción solo puede ser clasificada como ataque o no ataque.  
- En caso de tratar bloques o conjuntos de transacciones, las acciones deben ser consistentes, evitando contradicciones en la clasificación.  
- Opcionalmente, se pueden definir acciones compuestas, como clasificar transacciones de alto volumen o con ROI elevado, para priorizar la detección de ataques de mayor impacto económico.  

### Función de Recompensa
La función de recompensa \( R(s_t, a_t) \) tiene como objetivo incentivar la correcta identificación de ataques tipo sándwich y penalizar los errores de clasificación. Se propone un esquema de recompensa que combina precisión y relevancia económica:  

\[
R(s_t, a_t) = 
\begin{cases} 
+1 \cdot \text{Volume}_t & \text{si la predicción es correcta} \\
-1 \cdot \text{Volume}_t & \text{si la predicción es incorrecta}
\end{cases}
\]  

Este enfoque permite al agente priorizar la detección de ataques con mayor volumen o ROI**ACÁ YO CREO QUE PODRÍA SER CON ROI, PREGUNTAR A JULIÁN**, alineando la política de aprendizaje con el objetivo de capturar transacciones de mayor relevancia económica.  

### Política Óptima
La **política óptima** \( \pi^* \) se define como la estrategia que maximiza la recompensa acumulada esperada a lo largo del tiempo:  

\[
\pi^*(s) = \arg\max_a \mathbb{E}\Big[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \Big]
\]  

donde \( \gamma \) es el factor de descuento que pondera la importancia de recompensas futuras. La política óptima permite al agente:  
- Identificar transacciones con alta probabilidad de ser ataques tipo sándwich.  
- Priorizar la detección de ataques con mayor volumen o ROI.  
- Minimizar falsos positivos y negativos, equilibrando precisión y cobertura en la identificación de transacciones MEV.
