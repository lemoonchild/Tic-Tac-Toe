# utils/alphaBetaPruning/minimax_ab.py
from TicTacToe import TicTacToe
from typing import Tuple

def alpha_beta(node: TicTacToe,
               depth: int,
               alpha: float,
               beta: float,
               max_player: bool) -> Tuple[float, int]:
    """
    Devuelve (valor_est, nodos_explorados)
    usando poda α–β.
    """
    nodes = 1
    util = node.utility()
    if util is not None or depth == 0:
        return (util if util is not None else node.heuristic(), nodes)

    if max_player:
        value = float('-inf')
        for move in node.available_moves():
            child = node.clone()
            child.make_move(move)
            v, n = alpha_beta(child, depth-1, alpha, beta, False)
            nodes += n
            value = max(value, v)
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # poda
        return value, nodes
    else:
        value = float('inf')
        for move in node.available_moves():
            child = node.clone()
            child.make_move(move)
            v, n = alpha_beta(child, depth-1, alpha, beta, True)
            nodes += n
            value = min(value, v)
            beta = min(beta, value)
            if alpha >= beta:
                break  # poda
        return value, nodes
