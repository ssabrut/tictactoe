from environment import Environment
from tictactoe import X_SYMBOL, O_SYMBOL

class Agent:
    def __init__(self, symbol):
        self.env = Environment()

    def __minimax(self, board, depth, is_maximizing):
        result = self.env.terminal_state()
        if result is not None:
            if result == X_SYMBOL:
                return 1 + depth
            elif result == O_SYMBOL:
                return -1 + depth
            else:
                return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = X_SYMBOL
                        score = self.__minimax(board, depth + 1, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = O_SYMBOL
                        score = self.__minimax(board, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score
    
    def invoke(self, board):
        best_score = float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = O_SYMBOL
                    score = self.__minimax(board, 0, True)
                    board[i][j] = ''
                    if score < best_score:
                        best_score = score
                        best_move = (i,j)
        return best_move