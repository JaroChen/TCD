# tic_tac_toe/game.py
#  1.方法1-初始化棋盘：返回一个3*3的空格列表来表示棋盘
#  2.方法2-打印棋盘状态
#  3.方法3-接受玩家的输入：确保玩家可以输入移动，同时，需要检查移动是否有效
#  4.方法4-玩家标记：在棋盘上放置玩家的标记，并检查是否合法【落棋子】
#  5.方法5-检查游戏是否有赢家：检查哪个玩家赢得了比赛【依次检查行、列、对角线】
#  6.方法6-检查游戏是否平局：棋盘满了，就没有赢家

#  7.主程序串方法做循环：初始化棋盘->定义当前玩家X先走->打印棋盘最初状态->玩家输入->落棋子->依次if判断是赢还是平局->切换玩家

#  8.增加了minmax方法，合并到主方法中修改

#  9.增加了悔棋的操作（仅限一步）

#  10.增加对手的策略(基础防守&必胜策略)，提升对手的智能化【先做10，后做9】

#  11.增加A-B方法，优化minmax算法

#  12.增加用户选择模式(人vs智障、人vs人、智障vs智障)，并将玩家操作和智障操作，封装成一个方法：player_move和ai_move

#  13.增加一个重新开始的功能

# from minimax import find_best_move
import copy
from Assignment_3.oppoents.tic_tac_toe_oppoent import  opponent_move
from Assignment_3.utils.common_functions import check_winner
from Assignment_3.utils.common_functions import get_game_mode

def initialize_board(size=3):
    # return [[' ' for _ in range(3)] for _ in range(3)]
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board):
    # print("\n".join(["|".join(row) for row in board]))
    for row in board:
        print(' | '.join(row))
        print('-' * (3 * len(board[0]) - 1))

def get_player_move(board):
    while True:                                     # add a quit button
        move_input = input("Enter your move as 'row,col' or 'q' to quit: ").lower().strip()
        if move_input == 'q':
            print("Exiting game.")
            return None, None
        try:                                       # how to input character between row and col
            row, col = map(int, move_input.split(','))
            if row in range(1, len(board) + 1) and col in range(1, len(board[0]) + 1) and board[row-1][col-1] == ' ':
                if board[row-1][col-1] == ' ':     # check it if have character ‘ ’
                    return row - 1, col - 1
                else:
                    print("That space is already taken. Please try again.")
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")


def make_move(board, row, col, player):
    if board[row][col] == ' ':                 # exchange player A and player B
        board[row][col] = player
        return True
    return False


def player_move(board, player, board_history):
    while True:
        move = get_player_move(board)  # Same as base logic）
        if move == (None, None):       # check it if quit game
            return "quit"
        row, col = move
        if make_move(board, row, col, player):
            if player_wants_to_undo():  # 检查是否要悔棋
                undo_move(board_history)
                continue
            board_history.append(copy.deepcopy(board))  # 保存棋盘历史
            return "continue"
        else:
            print("This position is already taken. Choose another one.")


def ai_move(board, player, board_history):
    row, col = opponent_move(board, player)
    # Perform a move and save the history
    if make_move(board, row, col, player):
        print(f"AI ({player}) chose the location {row + 1},{col + 1}")
        board_history.append(copy.deepcopy(board))
    else:
        print("AI attempted to make an invalid move.")


def check_draw(board):     # Checking for a tie
    return all(all(cell != ' ' for cell in row) for row in board)

def player_wants_to_undo():
    answer = input("Would you like to reverse your move? (y/n): ").strip().lower()
    return answer == 'y'

def undo_move(board_history):
    if len(board_history) > 1:                                   # Make sure at least one move to regret.
        return board_history.pop()                               # Remove and return the state of the last move
    return board_history[0]                                      # If it is not possible to repent, return to the current state

def ask_for_restart():
    while True:
        response = input("Do you want to play again? (y/n): ").strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def tic_tac_toe():                                               # string methods together
    while True:                                                  #  add the game if coniute?
        game_over = False                                            # Marking the end of a game
        mode = get_game_mode()
        board = initialize_board()                                   # step1
        board_history = [copy.deepcopy(board)]                       # Initialize the game history
        current_player = 'A'                                         # Suppose 'A' is a human player and 'B' is an AI.
        while True:
            print_board(board)                                       # step2

            if mode == '1':                                          # Player vs AI
                # Tips: the expansion of the player's operational functions is all here.
                if current_player == 'A':
                    result = player_move(board, current_player, board_history)
                    if result == "quit":
                        game_over = True
                        break
                else:
                    ai_move(board, current_player, board_history)
            elif mode == '2':                                        # AI vs AI
                ai_move(board, current_player, board_history)
            elif mode == '3':                                        # Player vs Player
                result = player_move(board, current_player, board_history)
                if result == "quit":
                    game_over = True
                    break




    #  -----------------------------------v 1.0---------------------------------------
    #         # Tips: the expansion of the player's operational functions is all here.
    #             if current_player == 'A':
    #             move = get_player_move(board)                        # Same as base logic
    #             if move == (None, None):                             # step3 check it if quit game
    #                 break                                            # break the loop
    #             row, col = move
    #             if not make_move(board, row, col, current_player):
    #                 print("This position is already taken. Choose another one.")
    #                 continue
    #             if player_wants_to_undo():
    #                 board = undo_move(board_history)
    #                 continue
    #             make_move(board, row, col, 'A')
    #             board_history.append(copy.deepcopy(board))  # Save current board state
    #
    #         # AI's turn to find the best move using the Minimax algorithm
    #         else:
    #             # row, col = find_best_move(board)
    #             row, col = opponent_move(board,current_player)       #  Pass in the current object of the definition
    #             make_move(board, row, col, 'B')
    #             print(f"AI chose the location {row + 1},{col + 1}")
    #   -----------------------------------v 1.0---------------------------------------



            # Check if the game is over
            if check_winner(board, 'A'):
                print_board(board)
                print("A wins!")
                game_over = True                            # ask to restart
                break
            elif check_winner(board, 'B'):
                print_board(board)
                print("B wins!")
                game_over = True                           # ask to restart
                break
            elif check_draw(board):
                print_board(board)
                print("It's a tie!")
                game_over = True                           # ask to restart
                break

            current_player = 'B' if current_player == 'A' else 'A'      # Automatic player switching(Put it in the oppoent file method)

        if not game_over:                               # If the game doesn't end properly, it doesn't ask whether to restart or not
             continue

        # Game over, ask to restart
        if not ask_for_restart():
            print("Thanks for playing!")
            break                                       # quit game


if __name__ == "__main__":
    tic_tac_toe()
