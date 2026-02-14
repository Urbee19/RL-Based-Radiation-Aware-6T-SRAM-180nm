import numpy as np
import matplotlib.pyplot as plt
from environment import SRAMEnvironment
from dqn_agent import DQNAgent
from reward_function import calculate_reward

episodes = 100

env = SRAMEnvironment()
state_size = 6
action_size = 4

agent = DQNAgent(state_size, action_size)

reward_history = []
qcrit_history = []

for e in range(episodes):
    state = env.reset()
    total_reward = 0

    for time in range(20):
        action = agent.act(state)
        next_state, done = env.step(action)
        reward = calculate_reward(next_state)

        agent.train(state, action, reward, next_state)

        state = next_state
        total_reward += reward

    reward_history.append(total_reward)
    qcrit_history.append(state[0])

    print(f"Episode {e+1}/{episodes}, Reward: {total_reward:.3f}, Qcrit: {state[0]:.2f}")

# Plot reward convergence
plt.figure()
plt.plot(reward_history)
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("RL Reward Convergence")
plt.grid()
plt.show()

# Plot Qcrit improvement
plt.figure()
plt.plot(qcrit_history)
plt.xlabel("Episode")
plt.ylabel("Qcrit (fC)")
plt.title("Qcrit Improvement After RL")
plt.grid()
plt.show()
