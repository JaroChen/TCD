import unittest
from ..tic_tac_toe.game import initialize_board, make_move, check_winner, check_draw


class TestTicTacToe(unittest.TestCase):

    def test_board_initialization(self):
        board = initialize_board()
        expected_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(board, expected_board, "The board should be initialized with empty spaces.")

    def test_make_move(self):
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        self.assertEqual(board[0][0], 'X', "The top-left corner should be 'X'.")

    def test_winner(self):
        board = initialize_board()
        # Simulate a winning condition
        board[0] = ['X', 'X', 'X']
        self.assertTrue(check_winner(board, 'X'), "Player X should be the winner.")

    def test_draw(self):
        board = [['X' if (i + j) % 2 == 0 else 'O' for j in range(3)] for i in range(3)]
        board[1][1] = ' '  # Leave one space empty
        self.assertFalse(check_draw(board), "The board is not full, so it shouldn't be a draw.")
        board[1][1] = 'X'  # Fill the space to simulate a draw
        self.assertTrue(check_draw(board), "The board is full, so it should be a draw.")


# Other tests can include invalid move, board updating after each move, etc.

if __name__ == '__main__':
    unittest.main()
