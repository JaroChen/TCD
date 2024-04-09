# Minimax 算法实现，针对 Tic Tac Toe
# Defining Player Markers
PLAYER = 'A'
OPPONENT = 'B'


def evaluate(board):
    """
        Evaluates the state of the board and returns:
        +10 If the player wins
        -10 if opponent wins
        0 Draw
    """
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == PLAYER:
                return +10
            elif board[i][0] == OPPONENT:
                return -10
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == PLAYER:
                return +10
            elif board[0][i] == OPPONENT:
                return -10

    # check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] == PLAYER:
            return +10
        elif board[1][1] == OPPONENT:
            return -10

    # no winner
    return 0


def is_moves_left(board):
    """
    Check the board for empty squares
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False


def minimax(board, depth, is_max):
    """
    Minimax
    """
    score = evaluate(board)          # step 1： evaluate

    # If the player/opponent has won the board, return the evaluated value
    if score == 10 or score == -10:
        return score

    # if there are no more moves and no winners, return 0
    if not is_moves_left(board):     # step 2: is_moves_left
        return 0

    if is_max:
        best = -1000
        # Iterate the board
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    # recursive call minimax
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '  # Undoing a move
        return best
    else:
        best = 1000


        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best


def find_best_move(board):
    """
    Calculate and return the best position to move
    """
    best_val = -1000
    best_move = (-1, -1)

    # Iterate through all the grids to see the best place to move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)    #  Step 3: minmax
                board[i][j] = ' '

    # Iterate through all the grids to see where the best move is located If this move is evaluated higher, update the best move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move
