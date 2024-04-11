# Q-Learning 算法实现，针对 Tic Tac Toe
import numpy as np
import random
import pickle


class QLearningAgent:
    def __init__(self, game, player='A', epsilon=0.9, alpha=0.1, gamma=0.9, episodes=10000):
        self.game = game
        self.Q = {}  # Q-table
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.episodes = episodes
        self.player = player  # 'A' or 'B'

    def learn(self):
        for episode in range(self.episodes):
            self.game.reset()
            state = self.game.get_current_game_tuple()
            done = False

            while not done:
                available_positions = self.game.get_available_positions()
                if not available_positions:
                    break  # 如果没有可用位置，直接跳出循环

                if random.uniform(0, 1) < self.epsilon:
                    action = random.choice(available_positions)  # Explore
                else:
                    action = self._choose_action(state)  # Exploit

                # Take action and observe reward
                self.game.make_move(action, self.player)
                next_state = self.game.get_current_game_tuple()
                reward, done = self._get_reward(next_state)

                # Q-learning update rule
                old_value = self.Q.get((state, action), 0)
                next_max = max(self.Q.get((next_state, a), 0) for a in self.game.get_available_positions())

                new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
                self.Q[(state, action)] = new_value

                state = next_state

            # Decay epsilon
            if self.epsilon > 0.1:
                self.epsilon *= 0.99

    def choose_action(self, state):
        # print("state: ", state)
        actions = self.game.get_available_positions()
        if not actions:
            return None  # 如果没有可用动作，返回None

        values = [self.Q.get((state, a), 0) for a in actions]
        max_value = max(values, default=0)  # 使用 default 避免空序列
        max_actions = [actions[i] for i, v in enumerate(values) if v == max_value]
        return random.choice(max_actions) if max_actions else None

    # def choose_action(self, state):
    #     """ 公共接口，用于选择动作 """
    #     return self._choose_action(state)

    def _get_reward(self, next_state):
        if self.game.is_winner():
            return 1, True
        elif not self.game.get_available_positions():
            return 0, True
        else:
            return 0, False

    def save_policy(self):
        with open('tic_tac_toe_policy.pkl', 'wb') as f:
            pickle.dump(self.Q, f)

    def load_policy(self):
        with open('tic_tac_toe_policy.pkl', 'rb') as f:
            self.Q = pickle.load(f)