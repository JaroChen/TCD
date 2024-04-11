
# from minimax import find_best_move
import copy
from Assignment_3.oppoents.tic_tac_toe_oppoent import  opponent_move
from Assignment_3.utils.common_functions import check_winner
from Assignment_3.utils.common_functions import get_game_mode
from q_learning import QLearningAgent

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
        # 如果使用 Q-learning 代理
        if mode == '4':  # 假设选项4是使用 Q-learning 代理
            q_agent = QLearningAgent(game=YourGameEnvironmentHere)
            q_agent.load_policy()  # 加载预先训练好的策略

        while not game_over:
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
            elif mode == '4':
                # 使用 Q-learning 代理
                if current_player == 'A':
                    player_move(board, current_player, board_history)
                else:
                    # 调用 Q-learning 代理的移动
                    action = q_agent.choose_action(get_state(board), get_all_possible_moves(board))
                    make_move(board, *action, current_player)
                    board_history.append(copy.deepcopy(board))

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
