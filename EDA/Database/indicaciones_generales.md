Los datos fueron recolectados desde la página de Eigenphi, esta entidad estructura los datos emitidos por el EtherScan en la red de Ethereum 
Las variables que pude recolectar fueron:

## Variables del Dataset 

| **Variable**           | **Descripción**                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sandwich Count**     | Número de ataques tipo *sandwich* detectados.                                                                                             |
| **Attackers (EOA)**    | Cuántas cuentas (de personas o bots) actuaron como atacantes.                                                                             |
| **Victims (EOA)**      | Cuántas cuentas fueron víctimas de ataques sandwich.                                                                                      |
| **Volume**             | Cantidad total de tokens que se movieron en estos ataques (en ETH ).                                                              |
| **Profit**             | Ganancia neta que obtuvieron los atacantes después de pagar costos.                                                                        |
| **Cost**               | Lo que les costó hacer el ataque (principalmente tarifas de gas).                                                                          |
| **Revenue**            | Ingresos totales antes de restar costos (dinero que entró sin contar gastos).                                                             |
| **ROI (%)**            | Qué tan rentable fue el ataque. Si el ROI es 200%, significa que ganaron el doble de lo que gastaron.                                      |
| **> 1k Tx Count**      | Número de ataques sandwich en los que se movió más de 1,000 tokens o ETH.                                                                   |
| **> 1k Volume**        | Volumen total de esos ataques grandes.                                                                                                      |
| **> 1k Profit**        | Ganancia de los ataques grandes (más de 1,000 tokens).                                                                                      |
| **> 1k Cost**          | Costo total de esos ataques grandes.                                                                                                        |
| **> 1k Revenue**       | Ingresos brutos de esos ataques grandes.                                                                                                     |
| **> 1k ROI (%)**       | Rentabilidad (ROI) de los ataques grandes.                                                                                                    |
| **Mev-Bot Tx Count**   | Número total de transacciones hechas por bots MEV.                                                                                             |
| **Mev-Bot Volume**     | Todo el volumen que movieron los bots (en ETH o tokens).                                                                                        |
| **Mev-Bot Profit**     | Ganancia total de todos los bots analizados.                                                                                                      |
| **Mev-Bot Cost**       | Lo que gastaron los bots en gas y tarifas.                                                                                                        |
| **Mev-Bot Revenue**    | Ingresos totales (antes de restar costos) de todos los bots.                                                                                     |
| **MEV ROI (%)**        | Qué tan rentable fue la operación global de los bots.                                                                                               |

---