# Tic Tac Toe 的默认对手实现
# 1)检查必胜（Winning Move）：AI首先需要检查是否有可能一步获胜的机会，然后占据那个位置。
# 2)检查防守（Blocking Move）：如果玩家有一步获胜的机会，AI需要防守那个位置。
# 3)选择中心：如果中心是空的，AI通常会优先占据中心。
# 4)随机移动：如果上述策略都不适用，AI可以选择一个随机的合法移动【这里直接用minmax算法的最优随机移动】

# import random
from Assignment_3.utils.common_functions import check_winner
from Assignment_3.tic_tac_toe.minimax import find_best_move

def find_winning_move(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if check_winner(board, player):
                    return (i, j)                 # return a must-win move
                board[i][j] = ' '                 # undoing move

def find_blocking_move(board, opponent):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = opponent
                if check_winner(board, opponent):
                    return (i, j)                # return a opponent from winning
                board[i][j] = ' '

def opponent_move(board, player):
    # mark B
    opponent = 'B' if player == 'A' else 'A'

    # Check if there is a must-win move
    win_move = find_winning_move(board, player)
    if win_move:
        return win_move

    # Check if you need to stop your opponent from winning
    block_move = find_blocking_move(board, 'X' if player == 'O' else 'X')
    if block_move:
        return block_move

    # board center strategy: if the center is empty, occupy the center
    if board[1][1] == ' ':
        return (1, 1)

    # Otherwise a legal move is randomly selected
    # moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    # return random.choice(moves) if moves else None

    # If there are no sure wins and no chance of defense, use the Minimax algorithm to find the best moves
    return find_best_move(board)

