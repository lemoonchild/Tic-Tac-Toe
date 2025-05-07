# utils/MCTS/simulateGame.py
from TicTacToe import TicTacToe
from typing import Tuple
from utils.MCTS.selectBestPlay import select_best_move

def simulate_game(sims: int, c: float, starting_player: str) -> Tuple[int,int]:
    """
    Simula una partida completa usando MCTS en cada turno.
    Devuelve (resultado, simulaciones_totales)
    """
    state = TicTacToe(turn=starting_player)
    total_sims = 0

    while not state.is_terminal():
        move, used = select_best_move(state, sims=sims, c=c)
        total_sims += used
        state.make_move(move)

    return state.utility(), total_sims
