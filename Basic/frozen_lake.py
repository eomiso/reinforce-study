import gym

env = gym.make('FrozenLake-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())  # take a random action_space
    if env.done:
        break
env.close()
