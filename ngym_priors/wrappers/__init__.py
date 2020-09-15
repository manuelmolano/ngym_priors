#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:15:15 2020

@author: molano
"""
from ngym_priors.wrappers.reaction_time import ReactionTime
from ngym_priors.wrappers.variable_nch import Variable_nch
from ngym_priors.wrappers.trial_hist_ev import TrialHistoryEvolution
from ngym_priors.wrappers.variable_mapping import VariableMapping
from ngym_priors.wrappers.time_out import TimeOut
from ngym_priors.wrappers.noise import Noise

ALL_WRAPPERS = {'Noise-v0': 'ngym_priors.wrappers.noise:Noise',
                'TrialHistoryEv-v0':
                    'ngym_priors.wrappers.trial_hist_ev:TrialHistoryEvolution',
                'VariableMapping-v0':
                    'ngym_priors.wrappers.trial_hist_ev:VariableMapping',
                'Variable_nch-v0':
                    'ngym_priors.wrappers.variable_nch:Variable_nch',
                'TimeOut-v0':
                    'ngym_priors.wrappers.time_out:TimeOut'
                }

def all_wrappers():
    return sorted(list(ALL_WRAPPERS.keys()))
