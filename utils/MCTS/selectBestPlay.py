# utils/MCTS/selectBestPlay.py
from typing import Tuple
from TicTacToe import TicTacToe
from utils.MCTS.mcts import mcts

def select_best_move(state: TicTacToe,
                     sims: int = 100,
                     c: float = 1.414) -> Tuple[Tuple[int,int], int]:
    """
    Retorna (mejor_move, simulaciones_usadas)
    """
    return mcts(state, n_simulations=sims, c_param=c)
