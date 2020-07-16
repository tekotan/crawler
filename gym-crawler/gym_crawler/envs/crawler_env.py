import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

import client
class FooEnv(gym.Env):
  metadata = {'render.modes': ['human']}

    def __init__(self):
        action_low, action_high = 0, 90
        obs_low, obs_high = 0, 1100 # in meters
        num_servos = 12
        self.action_space = spaces.Box(action_low, action_high, shape=((num_servos,)))
        self.observation_space = spaces.Box(obs_low, obs_high, shape=((num_servos + 1),))
        self.curr_state = None

    def step(self, action):
        client.set_speed(action)
        next_state = client.get_state()
        reward = self.get_reward(self.curr_state, next_state)
        done = False
        return obs, reward, done, None

    def reset(self):
        self.curr_state = client.get_state()
        return self.curr_state

    def get_reward(self, curr_state, next_state):
        curr_distance = curr_state[num_servos]
        next_distance = next_state[num_servos]
        return next_distance - curr_distance
        
    def render(self, mode='human', close=False):
        pass