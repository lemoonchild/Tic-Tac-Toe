from typing import List, Optional, Tuple
import copy

class TicTacToe:
    def __init__(self, board: Optional[List[List[str]]] = None, turn: str = 'X'):
        # 'board' es una matriz 3×3 con 'X', 'O' o ''.
        self.board = board if board else [['']*3 for _ in range(3)]
        self.turn = turn  # 'X' o 'O'

    def clone(self) -> 'TicTacToe':
        # Retorna una copia profunda del estado
        return TicTacToe(copy.deepcopy(self.board), self.turn)

    def available_moves(self) -> List[Tuple[int,int]]:
        # Lista de casillas vacías
        return [(i,j)
                for i in range(3)
                for j in range(3)
                if self.board[i][j] == '']

    def make_move(self, move: Tuple[int,int]) -> None:
        i,j = move
        self.board[i][j] = self.turn
        self.turn = 'O' if self.turn == 'X' else 'X'

    def is_terminal(self) -> bool:
        return self.winner() is not None or not self.available_moves()

    def winner(self) -> Optional[str]:
        # Comprueba filas, columnas y diagonales
        lines = []
        lines += self.board                                   # filas
        lines += list(zip(*self.board))                       # columnas
        lines += [[self.board[i][i] for i in range(3)]]       # diag \
        lines += [[self.board[i][2-i] for i in range(3)]]     # diag /
        for line in lines:
            if line.count(line[0]) == 3 and line[0] in ('X','O'):
                return line[0]
        return None

    def utility(self) -> int:
        # +1 si gana X, -1 si gana O, 0 empate o no terminal
        w = self.winner()
        if w == 'X': return 1
        if w == 'O': return -1
        if not self.available_moves(): return 0
        return None  # todavía no terminal
    
    def heuristic(self) -> float:
        score = 0

        lines = []
        # Filas
        lines += self.board
        # Columnas
        lines += [list(col) for col in zip(*self.board)]
        # Diagonales
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2-i] for i in range(3)])

        for line in lines:
            x_count = line.count('X')
            o_count = line.count('O')
            # Si la línea está abierta para X
            if o_count == 0 and x_count > 0:
                if x_count == 2:
                    score += 10
                else:  # x_count == 1
                    score += 1
            # Si la línea está abierta para O
            if x_count == 0 and o_count > 0:
                if o_count == 2:
                    score -= 10
                else:  # o_count == 1
                    score -= 1

        # Bonus de posición
        # Centro
        if self.board[1][1] == 'X':
            score += 3
        # Esquinas
        for i,j in [(0,0),(0,2),(2,0),(2,2)]:
            if self.board[i][j] == 'X':
                score += 1

        return score
