# Connect 4 游戏逻辑
#  1.方法1-初始化棋盘：返回一个6*7的空格列表来表示棋盘
#  2.方法2-打印棋盘状态
#  3.方法3-接受玩家的输入：确保玩家可以输入移动，同时，需要检查移动是否有效
#  4.方法4-落子（不要忘记从列的底部开始）
#  5.方法5-检查游戏是否有赢家：检查哪个玩家赢得了比赛【依次检查行、列、对角线】
#  6.方法6-检查游戏是否平局：棋盘满了，就没有赢家

#  7.主程序串方法做循环：初始化棋盘->定义当前玩家X先走->打印棋盘最初状态->玩家输入->落棋子->依次if判断是赢还是平局->切换玩家


# connect_4/game.py

def initialize_board(rows=6, cols=7):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    for row in reversed(board):           # Printing the board from the top
        print(' | '.join(row))
    print('-' * (2 * len(board[0]) - 1))

def get_player_move(board):
    while True:
        move_input = input("Select a column to place (1-7) or enter 'q' to quit: ").lower().strip()
        if move_input == 'q':
            print("Exiting game.")
            return None
        if move_input.isdigit() and 1 <= int(move_input) <= 7:
            col = int(move_input) - 1
            if board[0][col] == ' ':
                return col
            else:
                print("This column is full, please select another column.")
        else:
            print("Invalid input, please enter a number from 1 to 7.")

def make_move(board, col, player):
    for row in reversed(board):    # Starting from the bottom to find empty spaces
        if row[col] == ' ':
            row[col] = player
            return

def check_winner(board, player):
    rows, cols = len(board), len(board[0])

    # check rows
    for row in range(rows):
        for col in range(cols - 3):
            if all(board[row][col+i] == player for i in range(4)):
                return True

    # check cols
    for col in range(cols):
        for row in range(rows - 3):
            if all(board[row+i][col] == player for i in range(4)):
                return True

    # check diagonals(from top left to bottom right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(board[row+i][col+i] == player for i in range(4)):
                return True

    # check diagonals(from top right to bottom left)
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(board[row-i][col+i] == player for i in range(4)):
                return True

    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def connect_four():
    board = initialize_board()
    current_player = 'A'
    while True:
        print_board(board)
        col = get_player_move(board)
        if col is None:  # quit button
            break
        make_move(board, col, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a tie!")
            break
        current_player = 'B' if current_player == 'A' else 'A'

if __name__ == "__main__":
    connect_four()
