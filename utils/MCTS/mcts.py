# utils/MCTS/mcts.py
from TicTacToe import TicTacToe
from utils.MCTS.mcts_node import MCTSNode
import random

def rollout(state: TicTacToe) -> float:
    """
    Juega aleatoriamente hasta llegar a estado terminal.
    Retorna +1/0/–1 según utilidad para X.
    """
    current = state.clone()
    while not current.is_terminal():
        move = random.choice(current.available_moves())
        current.make_move(move)
    return current.utility()

def mcts(root_state: TicTacToe,
         n_simulations: int = 100,
         c_param: float = 1.414) -> tuple:
    """
    Ejecuta MCTS desde root_state.
    Retorna el mejor movimiento y el número de simulaciones.
    """
    root = MCTSNode(root_state)

    for _ in range(n_simulations):
        node = root
        # 1. SELECCIÓN
        while node.is_fully_expanded() and not node.state.is_terminal():
            node = node.best_child(c_param)
        # 2. EXPANSIÓN
        if not node.state.is_terminal():
            node = node.expand()
        # 3. SIMULACIÓN
        reward = rollout(node.state)
        # 4. RETROPROPAGACIÓN
        while node is not None:
            node.visits += 1
            node.reward += reward
            node = node.parent

    # Elegir el hijo más visitado
    best_child = max(root.children, key=lambda c: c.visits)
    return best_child.move, n_simulations
