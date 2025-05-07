# utils/MCTS/mcts_node.py
from typing import List, Optional
import math
import random
from TicTacToe import TicTacToe

class MCTSNode:
    def __init__(self,
                 state: TicTacToe,
                 parent: Optional['MCTSNode'] = None,
                 move=None):
        self.state = state
        self.parent = parent
        self.move = move                # el movimiento que llevó a este nodo
        self.children: List[MCTSNode] = []
        self.visits = 0
        self.reward = 0.0
        # movimientos aún no explorados desde este estado
        self.untried_moves = state.available_moves()

    def is_fully_expanded(self) -> bool:
        return len(self.untried_moves) == 0

    def best_child(self, c_param: float) -> 'MCTSNode':
        # UCT = w_i/n_i + c * sqrt(2 ln N / n_i)
        choices = []
        for child in self.children:
            uct_value = (child.reward / child.visits) + \
                        c_param * math.sqrt(2 * math.log(self.visits) / child.visits)
            choices.append((uct_value, child))
        return max(choices, key=lambda x: x[0])[1]

    def expand(self) -> 'MCTSNode':
        move = self.untried_moves.pop()
        next_state = self.state.clone()
        next_state.make_move(move)
        child = MCTSNode(next_state, parent=self, move=move)
        self.children.append(child)
        return child
