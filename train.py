from envs.ethereum_env import EthereumEnv
from agents.dqn_agent import DQNAgent
import numpy as np

env = EthereumEnv()
agent = DQNAgent(state_dim=3, action_dim=3)

EPISODES = 500

for ep in range(EPISODES):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        agent.train_step()
        state = next_state
        total_reward += reward

    print(f"Episode {ep+1}, Total Reward: {total_reward:.2f}")
