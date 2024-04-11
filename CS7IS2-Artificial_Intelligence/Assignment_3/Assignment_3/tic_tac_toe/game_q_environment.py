import numpy as np

class TicTacToeEnvironment:
    def __init__(self, size=3):
        self.size = size
        self.board = np.zeros((size, size), dtype=int)
        self.current_player = 1  # Assuming 1 is 'A', -1 is 'B'

    def get_current_game_tuple(self):
        return tuple(tuple(row) for row in self.board)

    def get_available_positions(self):
        available_positions = []
        for i in range(self.size):
            for j in range(self.size):
                # print(f"检查位置 {i}, {j}: {self.board[i][j]}")  # 调试语句
                if self.board[i][j] == 0:
                    available_positions.append(i * self.size + j)
        return available_positions

        # positions = [i * self.size + j for i, row in enumerate(self.board) for j, cell in enumerate(row) if cell == ' ']
        # return positions

    def make_move(self, position, player):
        x, y = position
        if self.board[x][y] == ' ':
            self.board[x][y] = player
            self.current_player = -self.current_player  # Switch player
            return True
        return False

    def reset(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.current_player = 1

    def is_winner(self):
        # Check rows, columns and diagonals for a win
        for i in range(self.size):
            if abs(sum(self.board[i, :])) == self.size:  # Check row
                return True
            if abs(sum(self.board[:, i])) == self.size:  # Check column
                return True

        # Check diagonals
        if abs(sum(self.board.diagonal())) == self.size or abs(sum(np.fliplr(self.board).diagonal())) == self.size:
            return True

        return False
