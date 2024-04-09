import unittest
from ..connect_4.game import initialize_board, make_move, check_winner, check_draw

class TestConnectFour(unittest.TestCase):

    def test_board_initialization(self):
        """check if the board is initialized correctly."""
        board = initialize_board()
        self.assertEqual(len(board), 6)
        self.assertEqual(len(board[0]), 7)
        self.assertTrue(all(cell == ' ' for row in board for cell in row))

    def test_make_move(self):
        """check if a move is made correctly."""
        board = initialize_board()
        make_move(board, 3, 'A')  # Drop a piece in the fourth column
        # Check if the piece is at the bottom of the column
        self.assertEqual(board[-1][3], 'A')

    def test_winner_horizontal(self):
        """check rows win condition."""
        board = initialize_board()
        for col in range(4):
            make_move(board, col, 'A')
        self.assertTrue(check_winner(board, 'A'))

    def test_winner_vertical(self):
        """check cols win condition."""
        board = initialize_board()
        for _ in range(4):
            make_move(board, 0, 'A')  # Drop four 'A's in the first column
        self.assertTrue(check_winner(board, 'A'))

    def test_winner_diagonal(self):
        """check diagonal win condition."""
        board = initialize_board()
        for idx in range(4):
            for fill_idx in range(idx):
                make_move(board, idx, 'B')  # Fill with 'B' to make 'A' fall into a diagonal
            make_move(board, idx, 'A')
        self.assertTrue(check_winner(board, 'A'))

    def test_draw(self):
        """check draw condition."""
        board = [['A' if (row+col) % 2 == 0 else 'B' for col in range(7)] for row in range(6)]
        self.assertTrue(check_draw(board))

# More tests can be added as needed, such as checking for illegal moves, preventing moves when a column is full, etc.

if __name__ == '__main__':
    unittest.main()
