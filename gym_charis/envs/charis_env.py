import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self):
        pass
    def step(self, action):
        pass
    def reset(self):
        pass
    def render(self, mode='human'):
        # https://github.com/openai/gym/blob/b5a3367fd54bb3965977d30d2b0747d450e21536/gym/envs/unittest/memorize_digits.py
        pass
    def close(self):
        pass
