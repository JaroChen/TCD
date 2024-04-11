# Q-Learning 算法实现，针对 Tic Tac Toe
import numpy as np
import random
import pickle


class QLearningAgent:
    def __init__(self, game, epsilon=0.9, alpha=0.1, gamma=0.9, episodes=10000):
        self.game = game
        self.Q = {}  # Q-table
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.episodes = episodes
        self.player = 'A'

    def learn(self):
        for episode in range(self.episodes):
            self.game.reset()
            state = self.game.get_current_game_tuple()
            done = False

            while not done:
                if random.uniform(0, 1) < self.epsilon:
                    action = random.choice(self.game.get_available_positions())  # Explore
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

    def _choose_action(self, state):
        actions = self.game.get_available_positions()
        values = [self.Q.get((state, a), 0) for a in actions]
        max_value = max(values)
        max_actions = [actions[i] for i, v in enumerate(values) if v == max_value]
        return random.choice(max_actions)

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

