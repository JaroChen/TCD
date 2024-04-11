import copy
import numpy as np
from Assignment_3.oppoents.tic_tac_toe_oppoent import opponent_move
from Assignment_3.utils.common_functions import check_winner as base_check_winner
from Assignment_3.tic_tac_toe.q_learning import QLearningAgent


class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = self.initialize_board(size)
        self.current_player = 'A'
        self.board_history = [copy.deepcopy(self.board)]
        self.game_mode = self.get_game_mode()
        # self.q_agent = None  # Q-Learning代理初始化为None
        self.q_agent = QLearningAgent(game=YourGameEnvironment(self))

    def initialize_board(self, size):
        return [[' ' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * (3 * len(self.board[0]) - 1))

    def get_game_mode(self):
        print("Select game mode:")
        print("1. Player vs AI (Minimax)")
        print("2. AI vs AI (Minimax vs Q-Learning)")
        print("3. Player vs Player")
        print("4. Player vs AI (Q-Learning)")               # 添加 Q 学习模式
        return input("Enter your choice (1/2/3/4): ").strip()

    def get_player_move(self):
        move_input = input(
            f"Player {self.current_player}, enter your move as 'row,col' or 'q' to quit: ").lower().strip()
        if move_input == 'q':
            print("Exiting game.")
            return None, None
        try:
            row, col = map(int, move_input.split(','))
            return row - 1, col - 1
        except ValueError:
            print("Invalid input. Please enter two numbers separated by ','.")
            return None, None

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            self.board_history.append(copy.deepcopy(self.board))
            return True
        return False

    def undo_move(self):
        if len(self.board_history) > 1:
            self.board_history.pop()
            self.board = copy.deepcopy(self.board_history[-1])

    def check_winner(self):
        return base_check_winner(self.board, self.current_player)

    def check_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def ask_for_restart(self):
        response = input("Do you want to play again? (y/n): ").strip().lower()
        return response == 'y'

    def player_action(self):
        move = self.get_player_move()
        if move == (None, None):
            return False
        row, col = move
        if not self.make_move(row, col, self.current_player):
            print("This position is already taken. Choose another one.")
        return True

    def ai_action(self):
        row, col = opponent_move(self.board, self.current_player)
        self.make_move(row, col, self.current_player)
        print(f"AI ({self.current_player}) chose the location {row + 1},{col + 1}")

    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'A' else 'A'

# add q_learning_agent

    def init_q_agent(self):
        # 初始化Q-Learning代理
        self.q_agent = QLearningAgent(self)
        self.q_agent.load_policy()  # 加载已经训练好的策略

    def q_agent_action(self):
        # Q-Learning代理决定下一步
        state = self.get_current_game_tuple()
        action = self.q_agent._choose_action(state)
        row, col = divmod(action, self.size)  # 假设action是一个0到size^2-1的整数
        self.make_move(row, col, 'B')
        print(f"Q-Agent ('B') chose the location {row + 1},{col + 1}")

    def get_current_game_tuple(self):
        # 返回当前游戏状态的元组表示，供Q-Learning使用
        return tuple(' '.join(row) for row in self.board)

    def get_available_positions(self):
        # 返回可用位置的列表，供Q-Learning使用
        return [i * self.size + j for i, row in enumerate(self.board) for j, cell in enumerate(row) if cell == ' ']

    def play_game(self):
        self.board = self.initialize_board(self.size)
        self.board_history = [copy.deepcopy(self.board)]
        self.current_player = 'A'
        game_over = False

        while not game_over:
            self.print_board()
            if self.game_mode == '1' or (self.game_mode == '3' and self.current_player == 'A'):
                if not self.player_action():
                    break
            elif self.game_mode == '2' or self.current_player == 'B':
                self.ai_action()

            if self.check_winner():
                self.print_board()
                print(f"{self.current_player} wins!")
                game_over = True
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                game_over = True
            if self.game_mode == '4':                        # q_learning
                self.init_q_agent()
                while True:
                    if self.game_mode == '4' and self.current_player == 'B':
                        # 使用 Q-Learning 代理选择动作
                        state = self.game.get_current_game_tuple()
                        action = self.q_agent.choose_action(state)
                        self.make_move(*action, self.current_player)
                    else:
                        # 处理其他模式的逻辑
                        pass
                        # self.q_agent_action()
            if not game_over:
                self.switch_player()

            if game_over and self.ask_for_restart():
                game_over = False


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
