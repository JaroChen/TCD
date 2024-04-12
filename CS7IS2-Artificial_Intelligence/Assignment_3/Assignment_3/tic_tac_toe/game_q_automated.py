import copy
import numpy as np
from Assignment_3.oppoents.tic_tac_toe_oppoent import opponent_move
from Assignment_3.utils.common_functions import check_winner as base_check_winner
from Assignment_3.tic_tac_toe.q_learning import QLearningAgent
from Assignment_3.tic_tac_toe.game_q_environment import TicTacToeEnvironment

class TicTacToe:
    def __init__(self, size=3, game_mode='4'):  # 默认选择 Q-Learning
        self.size = size
        self.board = self.initialize_board(size)
        self.current_player = 'A'
        self.board_history = [copy.deepcopy(self.board)]
        self.game_mode = game_mode  # 设置为固定的游戏模式
        self.environment = TicTacToeEnvironment(size)
        self.q_agent = QLearningAgent(self.environment)

    def initialize_board(self, size):
        return [[' ' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * (3 * len(self.board[0]) - 1))

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            self.board_history.append(copy.deepcopy(self.board))
            return True
        return False

    def check_winner(self):
        return base_check_winner(self.board, self.current_player)

    def check_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'A' else 'A'

    def get_current_game_tuple(self):
        return tuple(' '.join(row) for row in self.board)

    def get_available_positions(self):
        return [i * self.size + j for i, row in enumerate(self.board) for j, cell in enumerate(row) if cell == ' ']

    def ai_action(self):
        if self.game_mode == '4':  # 使用 Q-Learning 策略
            action = self.q_agent.choose_action(self.get_current_game_tuple())
            if action is not None:
                row, col = divmod(action, self.size)
                self.make_move(row, col, self.current_player)
                print(f"Q-Agent ('{self.current_player}') chose the location {row + 1},{col + 1}")
        else:
            # 使用Minimax或其他AI策略
            row, col = opponent_move(self.board, self.current_player)
            self.make_move(row, col, self.current_player)
            print(f"AI ({self.current_player}) chose the location {row + 1},{col + 1}")

    def play_game(self):
        self.board = self.initialize_board(self.size)
        self.board_history = [copy.deepcopy(self.board)]
        game_over = False

        while not game_over:
            self.print_board()
            self.ai_action()  # 始终使用AI策略动作

            if self.check_winner():
                self.print_board()
                print(f"{self.current_player} wins!")
                game_over = True
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                game_over = True

            if not game_over:
                self.switch_player()

if __name__ == "__main__":
    game = TicTacToe(game_mode='4')  # 设置游戏模式
    game.play_game()
