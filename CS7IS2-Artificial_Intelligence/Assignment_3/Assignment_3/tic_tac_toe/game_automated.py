# 修改find_best_move，来将用户输入改为自动
import copy
import random
from Assignment_3.tic_tac_toe.game import make_move,initialize_board,check_draw,check_winner
from Assignment_3.tic_tac_toe.minimax import minimax

def get_available_positions(board):
    available_positions = []
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == ' ':
                available_positions.append((row_index, col_index))
    return available_positions

def get_random_move(board):
    available_positions = get_available_positions(board)
    return random.choice(available_positions) if available_positions else (None, None)

def automated_player_move(board, player):
    # 这里可以实现更复杂的 AI 逻辑，目前使用随机选择
    row, col = get_random_move(board)
    make_move(board, row, col, player)
    return row, col

# 假设 opponent_move 函数的目的是选择最佳移动
# 这里使用随机选择来代替，但是您应该使用像 minimax 这样的策略来选择移动
def opponent_move(board, player):
    available_positions = get_available_positions(board)
    if not available_positions:  # 如果没有可用位置，返回None
        return None, None
    # 选择随机的移动
    return random.choice(available_positions)


# 自动化
def find_best_move(board, player):
    PLAYER = 'A'
    OPPONENT = 'B'
    best_val = -float('inf') if player == PLAYER else float('inf')
    best_move = (-1, -1)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                board[i][j] = player
                current_val = minimax(board, 0, player == OPPONENT, -float('inf'), float('inf'))
                board[i][j] = ' '

                if player == PLAYER:
                    if current_val > best_val:
                        best_val = current_val
                        best_move = (i, j)
                else:
                    if current_val < best_val:
                        best_val = current_val
                        best_move = (i, j)

    return best_move


def tic_tac_toe_automated():
    board = initialize_board()
    board_history = [copy.deepcopy(board)]
    current_player = 'A'
    game_over = False

    while not game_over:
        if current_player == 'A':
            row, col = automated_player_move(board, 'A')
        else:
            row, col = automated_player_move(board, 'B')

        if row is None and col is None:
            game_over = True
            result = "draw"
        elif check_winner(board, current_player):
            game_over = True
            result = f"{current_player} wins"
        elif check_draw(board):
            game_over = True
            result = "draw"

        current_player = 'B' if current_player == 'A' else 'A'

    return result