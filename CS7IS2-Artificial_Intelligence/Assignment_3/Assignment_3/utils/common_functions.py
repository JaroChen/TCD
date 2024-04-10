# 可能被游戏或算法共用的功能，该文件就是通用API接口方法文件
# 1)oppoent 和 game 共用check_winner方法
# 2)用户选择模式

def check_winner(board, player):
    # check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # check cols
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board)-i-1] == player for i in range(len(board))):
        return True
    return False



def get_game_mode():
    print("Select game mode:")
    print("1. Player vs AI")
    print("2. AI vs AI")
    print("3. Player vs Player")
    choice = input("Enter your choice (1/2/3): ").strip()
    return choice