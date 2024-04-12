#  该部分是Connect 4 的完整 Q-Learning 游戏实现，结合了Connect Four 环境类和 Q-Learning 代理
#  该部分包括一个主游戏类，负责管理游戏流程、用户输入（如果需要的话）和 AI 的动作
import numpy as np
import copy
from Assignment_3.connect_4.game_q_environment import ConnectFourEnvironment
from Assignment_3.connect_4.q_learning import ConnectFourQLearningAgent

class ConnectFourGame:
    def __init__(self, rows=6, cols=7):
        self.current_player = 'A'  # 开始时设置初始玩家为 'A'
        self.environment = ConnectFourEnvironment(rows, cols)
        self.q_agent = ConnectFourQLearningAgent(self.environment)
        self.game_mode = self.get_game_mode()
        self.is_board_full = self.is_board_full()


    def get_game_mode(self):
        print("Select game mode:")
        print("1. Player vs Player")
        print("2. AI vs AI (Q-Learning)")
        print("3. Player vs AI (Q-Learning)")
        choice = input("Enter your choice (1/2/3): ").strip()
        return choice

    def switch_player(self):
        if self.current_player == 'A':
            self.current_player = 'B'
        else:
            self.current_player = 'A'

    def is_board_full(self):
        return not np.any(self.board == ' ')

    def play_game(self):
        # self.reset()  # 确保开始新游戏时棋盘是清空的
        game_over = False
        current_player = 'A'  # Player 'A'

        while not game_over:
            self.environment.print_board()               # 打印当前棋盘状态

            if self.game_mode == '1' or (self.game_mode == '3' and current_player == 'A'):  # Player vs Player
                move = self.get_player_move(current_player)

            elif self.game_mode == '2' :  # AI vs AI
                move = self.q_agent.choose_action(self.environment.get_current_game_tuple())
                if move is None:
                    print("No valid move available.")
                    continue

            elif self.game_mode == '3' and current_player == 'A':  # Player vs AI
                move = self.get_player_move(current_player)
            else:  # AI move in Player vs AI
                move = self.q_agent.choose_action(self.environment.get_current_game_tuple())
                if move is None:
                    print("No valid move available.")
                    continue

            if not self.environment.make_move(move, current_player):
                print("Invalid move. Try again.")
                continue

            if self.environment.is_winner(current_player):
                self.environment.print_board()
                print(f"Player {current_player} wins!")
                game_over = True
            elif not self.environment.get_available_positions():
                if self.environment.is_board_full():  # You need to implement this method to check if board is really full
                    self.environment.print_board()
                    print("It's a draw!")
                    game_over = True

            current_player = self.switch_player()  # Switch player

            if game_over and self.ask_for_restart():
                self.environment.reset()
                game_over = False
                current_player = 'A'  # Reset to player 'A'

    def get_player_move(self, player):
        try:
            col = int(input(f"Player's turn, choose column (0-{self.environment.cols-1}): "))
            return col
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_player_move(player)

    def ask_for_restart(self):
        restart = input("Do you want to play again? (y/n): ").lower()
        return restart == 'y'

if __name__ == "__main__":
    game = ConnectFourGame()
    game.play_game()
