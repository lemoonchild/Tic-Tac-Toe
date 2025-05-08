# Tic-Tac-Toe

Tic Tac Toe for IA Course

# Cuando el adversario ”X” es el jugador que inicia la partida.

| Var | Algoritmo        | Parámetros        | Starter | Vict_X | Empates | Vict_O | Costo_avg | Tiempo_avg |
| :-: | :--------------- | :---------------- | :------ | -----: | ------: | -----: | --------: | ---------: |
| V1  | minimaxNormal    | k=2               | X       |      0 |    1000 |      0 |     285.0 |     0.004s |
| V2  | minimaxNormal    | k=3               | X       |   1000 |       0 |      0 |    1474.0 |     0.021s |
| V3  | alphaBetaPruning | k=2               | X       |      0 |    1000 |      0 |     285.0 |     0.005s |
| V4  | alphaBetaPruning | k=3               | X       |   1000 |       0 |      0 |     946.0 |     0.014s |
| V5  | MCTS             | sims=200, C=1.0   | X       |   1000 |       0 |      0 |    1121.2 |     0.050s |
| V6  | MCTS             | sims=500, C=1.414 | X       |   1000 |       0 |      0 |    3077.0 |     0.142s |

# Cuando el adversario ”O” es el jugador que inicia la partida.

| Var | Algoritmo        | Parámetros        | Starter | Vict_X | Empates | Vict_O | Costo_avg | Tiempo_avg |
| :-: | :--------------- | :---------------- | :------ | -----: | ------: | -----: | --------: | ---------: |
| V1  | minimaxNormal    | k=2               | O       |      0 |       0 |   1000 |     278.0 |     0.004s |
| V2  | minimaxNormal    | k=3               | O       |      0 |    1000 |      0 |    1519.0 |     0.023s |
| V3  | alphaBetaPruning | k=3               | O       |      0 |    1000 |      0 |     946.0 |     0.014s |
| V4  | alphaBetaPruning | k=2               | O       |      0 |       0 |   1000 |     278.0 |     0.004s |
| V5  | MCTS             | sims=200, C=1.0   | O       |   1000 |       0 |      0 |    1372.0 |     0.058s |
| V6  | MCTS             | sims=500, C=1.414 | O       |   1000 |       0 |      0 |    3504.0 |     0.148s |
