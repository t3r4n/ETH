# Agente RL y entorno MempoolEnv

Especificación de partida (a validar con el tutor).

- Entorno: Gymnasium.
- Observación: ventana deslizante de H=10 observaciones, con K=5 submuestreadas
  en orden temporal (adaptación de Seoev et al., 2025, preprint arXiv:2510.14642).
  En ese paper la historia son estadísticas de subastas pasadas; aquí es una
  ventana de transacciones de la mempool.
- Variables por transacción: g, p, o, d, v, l, i, c (ver formulación).
- Acciones: {Ignore, Wait, Flag}.
- Recompensa: diferida, calculada contra el bloque confirmado (verdad terreno).
- Algoritmo: PPO.
- La dinámica de la mempool es exógena: las acciones no la alteran.

Pendiente: definir cómo se resuelve un episodio y cuándo se asigna la recompensa.
