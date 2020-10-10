#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:02:28 2020

@author: molano
"""

import neurogym as ngym
from neurogym.core import TrialWrapper
import numpy as np
import itertools as it


class PerfectIntegrator(TrialWrapper):
    """

    """
    metadata = {
        'description': 'Change ground truth probability based on previous' +
        'outcome.',
        'paper_link': 'https://www.biorxiv.org/content/10.1101/433409v3',
        'paper_name': 'Response outcomes gate the impact of expectations ' +
        'on perceptual decisions'
    }

    def __init__(self, env):
        super().__init__(env)
        try:
            self.n_ch = len(self.unwrapped.choices)  # max num of choices
        except AttributeError:
            raise AttributeError('task must have attribute choices')
        assert isinstance(self.unwrapped, ngym.TrialEnv), 'Task has to be TrialEnv'
        self.prev_choice = self.rng.choice(self.n_ch)  # random initialization
        self.prev_reward = 0
        self.cum_sum = np.zeros((self.n_ch,))
        self.stim_indx = self.env.observation_space.name['stimulus']
        self.obs_sh = self.env.observation_space.shape[0]

    def step(self, action):
        if self.env.t_ind >= self.env.start_t['decision']:
            act_io = np.argmax(self.cum_sum)+1
        else:
            act_io = 0
        obs, reward, done, info = self.env.step(act_io)
        if info['new_trial']:
            self.cum_sum = np.zeros((self.n_ch,))
        else:
            self.cum_sum += obs[self.stim_indx]
        obs = np.array([self.prev_choice, self.prev_reward])
        obs = np.concatenate((obs, np.zeros((self.obs_sh,))))
        self.prev_choice = act_io
        self.prev_reward = reward
        reward = action == info['gt']
        return obs, reward, done, info
