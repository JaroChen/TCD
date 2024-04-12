# 构建一个 Q-Learning 代理来学习和操作游戏
# Connect 4 游戏在垂直方向上有堆叠的特点，并且需要检查水平、垂直和对角线方向的连线

import numpy as np

class ConnectFourEnvironment:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)  # 0 表示空，1 表示玩家 A，-1 表示玩家 B
        # self.current_player = 1  # 1 代表玩家 'A'
    def print_board(self):
        """打印当前棋盘的状态，其中0表示空，1表示'A'，-1表示'B'。"""
        print("Current Board:")
        for row in self.board:
            print(' | '.join(str(x) for x in row))
            print('-' * (self.cols * 4 - 1))  # Adjust the number of dashes based on the number of columns

    def get_current_game_tuple(self):
        """返回棋盘状态的元组形式，以供学习算法使用。"""
        return tuple(tuple(row) for row in self.board)

    def get_available_positions(self):
        """返回棋盘上所有空位的列表。"""
        return [c for c in range(self.cols) if self.board[0, c] == 0]

    def make_move(self, col, player):
        """ 尝试在指定列放置玩家的棋子。 """
        for row in range(self.rows - 1, -1, -1):
            if self.board[row, col] == 0:
                self.board[row, col] = player
                return True
        return False  # If no space was available in the column
    def reset(self):
        """ 重置棋盘为初始状态。 """
        self.board = np.zeros((self.rows, self.cols), dtype=int)
        # self.current_player = 1

    def is_winner(self, player):
        """ 检查是否有玩家赢得了游戏。 """
        # 检查水平连线
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row, col + i] == player for i in range(4)):
                    return True

        # 检查垂直连线
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row + i, col] == player for i in range(4)):
                    return True

        # 检查对角线
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i, col + i] == player for i in range(4)):
                    return True
                if all(self.board[row + 3 - i, col + i] == player for i in range(4)):
                    return True

        return False
