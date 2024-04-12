import numpy as np
import random
from Assignment_3.connect_4.minimax import minimax,evaluate


def initialize_board(rows=6, cols=7):
    """ 初始化游戏板 """
    return np.full((rows, cols), ' ', dtype=str)

def drop_piece(board, col, player):
    """ 在指定列放入棋子 """
    for row in reversed(range(board.shape[0])):
        if board[row, col] == ' ':
            board[row, col] = player
            return True
    return False

def check_winner(board, player):
    """ 检查指定玩家是否赢得比赛 """
    rows, cols = board.shape
    # 检查所有四种赢得情况
    for r in range(rows):
        for c in range(cols-3):
            if all(board[r, c+i] == player for i in range(4)):
                return True
    for c in range(cols):
        for r in range(rows-3):
            if all(board[r+i, c] == player for i in range(4)):
                return True
    for r in range(rows-3):
        for c in range(cols-3):
            if all(board[r+i, c+i] == player for i in range(4)):
                return True
            if all(board[r+3-i, c+i] == player for i in range(4)):
                return True
    return False

def get_legal_moves(board):
    """ 返回可落子的列 """
    return [c for c in range(board.shape[1]) if board[0, c] == ' ']

def find_best_move(board, player):
    """ 使用 Minimax 算法找到最佳移动 """
    best_move = None
    best_score = -float('inf')
    for move in get_legal_moves(board):
        temp_board = np.copy(board)
        if drop_piece(temp_board, move, player):
            score = minimax(temp_board, depth=4, maximizingPlayer=False, alpha=-float('inf'), beta=float('inf'), player=player)
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def minimax(board, depth, maximizingPlayer, alpha, beta, player):
    """ Minimax 算法实现 """
    opponent = 'B' if player == 'A' else 'A'
    if depth == 0 or check_winner(board, player) or check_winner(board, opponent):
        return evaluate(board, player)

    if maximizingPlayer:
        max_eval = -float('inf')
        for move in get_legal_moves(board):
            temp_board = np.copy(board)
            if drop_piece(temp_board, move, player):
                eval = minimax(temp_board, depth-1, False, alpha, beta, player)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_legal_moves(board):
            temp_board = np.copy(board)
            if drop_piece(temp_board, move, opponent):
                eval = minimax(temp_board, depth-1, True, alpha, beta, player)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def connect_four_automated():
    """ 自动运行 Connect Four 游戏 """
    board = initialize_board()
    current_player = random.choice(['A', 'B'])  # 随机选择起手玩家
    while True:
        best_move = find_best_move(board, current_player)
        if best_move is None:     # 没有可行的移动
            print("Game Over. Draw.")
            break
        drop_piece(board, best_move, current_player)
        print("Board after " + current_player + " move:")
        print(board)
        if check_winner(board, current_player):
            print(current_player + " wins!")
            return f"{current_player} wins"  # 返回胜利结果
        current_player = 'B' if current_player == 'A' else 'A'

if __name__ == "__main__":
    connect_four_automated()
