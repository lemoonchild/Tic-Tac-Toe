# utils/alphaBetaPruning/simulateGame.py
from TicTacToe import TicTacToe
from typing import Tuple
from utils.alphaBetaPruning.selectBestPlay import select_best_move

def simulate_game(depth: int, starting_player: str) -> Tuple[int,int]:
    """
    Misma simulación que antes, pero usando α–β.
    """
    state = TicTacToe(turn=starting_player)
    total_nodes = 0

    while not state.is_terminal():
        move, nodes = select_best_move(state, depth)
        total_nodes += nodes
        state.make_move(move)

    return state.utility(), total_nodes
