import gym
from gym import spaces
import numpy as np

class EthereumEnv(gym.Env):
    """Custom Gym environment simulating simplified Ethereum node behavior"""
    
    def __init__(self):
        super(EthereumEnv, self).__init__()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=1, shape=(3,), dtype=np.float32)
        self.state = self._next_observation()
        self.step_count = 0
        self.max_steps = 100

    def _next_observation(self):
        return np.random.rand(3)

    def step(self, action):
        reward = self._calculate_reward(action)
        self.state = self._next_observation()
        self.step_count += 1
        done = self.step_count >= self.max_steps
        return self.state, reward, done, {}

    def reset(self):
        self.step_count = 0
        self.state = self._next_observation()
        return self.state

    def _calculate_reward(self, action):
        if action == 0:
            return np.random.uniform(0.5, 1.0)
        elif action == 1:
            return np.random.uniform(0.0, 0.5)
        else:
            return -0.1
