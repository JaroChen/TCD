# Connect 4 的默认对手实现
import numpy as np
import random


def initialize_connect_four_board(rows=6, cols=7):
    return np.full((rows, cols), ' ', dtype=str)

def check_winner_cf(board, player):
    rows, cols = board.shape
    # 检查水平连线
    for r in range(rows):
        for c in range(cols - 3):
            if board[r, c] == player and np.all(board[r, c:c+4] == player):
                return True
    # 检查垂直连线
    for r in range(rows - 3):
        for c in range(cols):
            if board[r, c] == player and np.all(board[r:r+4, c] == player):
                return True
    # 检查对角线
    for r in range(rows - 3):
        for c in range(cols - 3):
            if board[r, c] == player and all(board[r+i, c+i] == player for i in range(4)):
                return True
            if board[r+3, c] == player and all(board[r+3-i, c+i] == player for i in range(4)):
                return True
    return False

def get_legal_moves(board):
    # 返回最顶层空位的列号
    return [c for c in range(board.shape[1]) if board[0, c] == ' ']

def drop_piece(board, col, player):
    # 在选择的列放入棋子
    for row in reversed(range(board.shape[0])):
        if board[row, col] == ' ':
            board[row, col] = player
            break

def find_winning_move(board, player):
    # 找到必胜的移动
    for col in get_legal_moves(board):
        temp_board = board.copy()
        drop_piece(temp_board, col, player)
        if check_winner_cf(temp_board, player):
            return col
    return None

def find_blocking_move(board, player):
    # 找到阻挡对手必胜的移动
    opponent = 'A' if player == 'B' else 'B'
    return find_winning_move(board, opponent)

def opponent_move(board, player):
    # 优先找到必胜移动
    win_move = find_winning_move(board, player)
    if win_move is not None:
        return win_move

    # 检查并阻止对手必胜的移动
    block_move = find_blocking_move(board, player)
    if block_move is not None:
        return block_move

    # 如果没有必胜或阻挡对手的移动，选择中心列（如果可用）
    center_col = board.shape[1] // 2
    if center_col in get_legal_moves(board):
        return center_col

    # 如果中心列不可用，随机选择一个合法移动
    legal_moves = get_legal_moves(board)
    return random.choice(legal_moves) if legal_moves else None

