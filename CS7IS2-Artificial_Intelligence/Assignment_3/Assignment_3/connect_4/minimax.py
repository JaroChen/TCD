# 不同于tic_tac_toe的minmax，connect_4的minmax考虑游戏的四连规则和垂直堆叠特性
import numpy as np

# Defining constants for player markers
PLAYER = 'A'
OPPONENT = 'B'


def evaluate(board,player):
    """
    Evaluate the board for the Connect Four game.
    +1000 for PLAYER winning, -1000 for OPPONENT winning, 0 otherwise.
    """
    rows, cols = board.shape
    opponent = 'B' if player == 'A' else 'A'
    # Horizontal, vertical, and diagonal checks
    for r in range(rows):
        for c in range(cols - 3):
            line = board[r, c:c + 4]
            if np.all(line == PLAYER):
                return 1000
            elif np.all(line == OPPONENT):
                return -1000

    for c in range(cols):
        for r in range(rows - 3):
            line = board[r:r + 4, c]
            if np.all(line == PLAYER):
                return 1000
            elif np.all(line == OPPONENT):
                return -1000

    for r in range(rows - 3):
        for c in range(cols - 3):
            line = np.array([board[r + i, c + i] for i in range(4)])
            if np.all(line == PLAYER):
                return 1000
            elif np.all(line == OPPONENT):
                return -1000

            line = np.array([board[r + 3 - i, c + i] for i in range(4)])
            if np.all(line == PLAYER):
                return 1000
            elif np.all(line == OPPONENT):
                return -1000

    return 0


def is_moves_left(board):
    """
    Check if any cells are left empty in the board.
    """
    return np.any(board == ' ')


def minimax(board, depth, is_max, alpha, beta):
    """
    Minimax function with alpha-beta pruning for Connect Four.
    """
    score = evaluate(board)

    if score == 1000 or score == -1000:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -np.inf
        for c in range(board.shape[1]):
            for r in range(board.shape[0] - 1, -1, -1):
                if board[r, c] == ' ':
                    board[r, c] = PLAYER
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[r, c] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return best
    else:
        best = np.inf
        for c in range(board.shape[1]):
            for r in range(board.shape[0] - 1, -1, -1):
                if board[r, c] == ' ':
                    board[r, c] = OPPONENT
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[r, c] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return best


def find_best_move(board):
    """
    Determine the best move by evaluating the minimax function for each legal move.
    """
    best_val = -np.inf
    best_move = (-1, -1)
    for c in range(board.shape[1]):
        for r in range(board.shape[0] - 1, -1, -1):
            if board[r, c] == ' ':
                board[r, c] = PLAYER
                move_val = minimax(board, 0, False, -np.inf, np.inf)
                board[r, c] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (r, c)
                break  # Only evaluate the lowest available row in each column

    return best_move if best_move != (-1, -1) else None
