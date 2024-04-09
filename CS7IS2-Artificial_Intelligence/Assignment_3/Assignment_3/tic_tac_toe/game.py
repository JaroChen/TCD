# Tic Tac Toe 游戏逻辑
#  1.方法1-初始化棋盘：返回一个3*3的空格列表来表示棋盘
#  2.方法2-打印棋盘状态
#  3.方法3-接受玩家的输入：确保玩家可以输入移动，同时，需要检查移动是否有效
#  4.方法4-玩家标记：在棋盘上放置玩家的标记，并检查是否合法【落棋子】
#  5.方法5-检查游戏是否有赢家：检查哪个玩家赢得了比赛【依次检查行、列、对角线】
#  6.方法6-检查游戏是否平局：棋盘满了，就没有赢家

#  7.主程序串方法做循环：初始化棋盘->定义当前玩家X先走->打印棋盘最初状态->玩家输入->落棋子->依次if判断是赢还是平局->切换玩家

# tic_tac_toe/game.py

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
    # if board[row][col] == ' ':
    board[row][col] = player
    #     return True
    # return False

def check_winner(board, player):
    # check row
    for row in board:
        if all(s == player for s in row):
            return True
    # check col
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    # check diagonal
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board)-i-1] == player for i in range(len(board))):
        return True
    return False


def check_draw(board):     # Checking for a tie
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():        # string methods together
    board = initialize_board()                        # step1
    current_player = 'A'
    while True:
        print_board(board)                            # step2

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a tie!")
            break

        move = get_player_move(board)
        if move == (None, None):                      # step3 check it if quit game
            break
        row, col = move
        if not make_move(board, row, col, current_player):
            print("This position is already taken. Choose another one.")
            continue

        current_player = 'B' if current_player == 'A' else 'A'      # Automatic player switching


if __name__ == "__main__":
    tic_tac_toe()
