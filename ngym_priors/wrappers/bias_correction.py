#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  Feb  2020

@author: jorgedelpozolerida

"""

import neurogym as ngym
import numpy as np
from gym import Wrapper
from collections import deque


class BiasCorrection(Wrapper):
    metadata = {
        'description': 'Change number of active choices every ' +
        'block_nch trials. Always less or equal than original number.',
        'paper_link': None,
        'paper_name': None
    }

    def __init__(self, env, choice_w=1000):
        """
        block_nch: duration of each block containing a specific number
        of active choices
        prob_2: probability of having only two active choices per block
        """
        super().__init__(env)
        assert isinstance(self.unwrapped, ngym.TrialEnv), 'Task has to be TrialEnv'
        self.max_nch = len(self.unwrapped.choices)  # Max number of choices
        self.choice_w = choice_w
        self.choices = deque(maxlen=self.choice_w)
        self.ground_truth = deque(maxlen=self.choice_w)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        if info['new_trial']:
            self.choices.append(action)
            self.ground_truth.append(info['gt'])
            if info['performance'] == 1 and len(self.choices) == self.choice_w and\
               len(self.ground_truth) == self.choice_w:
                poss_chs = np.unique(self.ground_truth)
                factor = np.min([(1+np.sum(np.array(self.choices) == x)) /
                                 np.sum(np.array(self.ground_truth) == x)
                                 for x in poss_chs])
                reward = reward*factor
        return obs, reward, done, info
