import os
import logging
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from PIL import Image

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self, components_dir, target_path):
        self._viewer = None
        self._components = self._load_components(components_dir)
        self._target = Image.open(target_path)
        self._canvas = Image.new('RGB',
                                 (self._target.width, self._target.height),
                                 (255, 255, 255))

        self.observation_space = spaces.Box(0, 255,
                np.asarray(self._target).shape)
        self.action_space = spaces.Tuple((
            spaces.Discrete(len(self._components)),
            spaces.Box(low=-1.0, high=1.0, shape=(4,)),
        ))

    def _load_components(self, components_dir):
        components = []
        for f in os.listdir(components_dir):
            logging.info('loading component= %s', f)
            component_path = os.path.join(components_dir, f)
            component = Image.open(component_path)
            components.append(component)
        return components

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        # https://github.com/openai/gym/blob/master/docs/creating-environments.md
        # https://github.com/openai/gym/blob/b5a3367fd54bb3965977d30d2b0747d450e21536/gym/envs/unittest/memorize_digits.py

        if mode == 'rgb_array':
            return np.asarray(self._canvas)

        elif mode == 'human':
            from gym.envs.classic_control import rendering
            if self._viewer is None:
                self._viewer = rendering.SimpleImageViewer()
            self._viewer.imshow(np.asarray(self._canvas))
            return self._viewer.isopen

        assert 0, 'Render mode "%s" is not supported'%(mode)

    def close(self):
        if self._viewer is not None:
            self._viewer.close()
            self._viewer = None

if __name__ == '__main__':
    import time
    env = FooEnv('components/', 'target.jpg')
    env.render()
    time.sleep(20)

