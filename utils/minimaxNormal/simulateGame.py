import random
from collections import Counter
from TicTacToe import TicTacToe
from typing import Tuple
from utils.minimaxNormal.selectBestPlay import select_best_move


def simulate_game(depth: int, starting_player: str) -> Tuple[int, int]:
    """
    Devuelve (resultado, nodos_totales_explorados)
    - resultado: +1 victoria X, 0 empate, -1 victoria O
    """
    state = TicTacToe(turn=starting_player)
    total_nodes = 0

    while not state.is_terminal():
        move, nodes = select_best_move(state, depth)
        total_nodes += nodes
        state.make_move(move)

    return state.utility(), total_nodes
