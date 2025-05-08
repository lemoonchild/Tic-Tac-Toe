# utils/alphaBetaPruning/selectBestPlay.py
from typing import Tuple
from TicTacToe import TicTacToe
from utils.alphaBetaPruning.minimax_ab import alpha_beta

def select_best_move(state: TicTacToe, depth: int) -> Tuple[Tuple[int,int], int]:
    """
    Igual que en minimaxNormal, pero llamando a alpha_beta.
    """
    best_move = None
    total_nodes = 0

    if state.turn == 'X':
        best_val = float('-inf')
        for move in state.available_moves():
            child = state.clone()
            child.make_move(move)
            # α=-∞, β=+∞ al inicio
            v, n = alpha_beta(child, depth-1,
                              float('-inf'), float('inf'),
                              False)
            total_nodes += n
            if v > best_val:
                best_val = v
                best_move = move
    else:
        best_val = float('inf')
        for move in state.available_moves():
            child = state.clone()
            child.make_move(move)
            v, n = alpha_beta(child, depth-1,
                              float('-inf'), float('inf'),
                              True)
            total_nodes += n
            if v < best_val:
                best_val = v
                best_move = move

    return best_move, total_nodes
