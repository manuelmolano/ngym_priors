#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:15:15 2020

@author: molano
"""
from ngym_priors.wrappers.variable_reaction_time import VariableReactionTime
from ngym_priors.wrappers.variable_nch import Variable_nch
from ngym_priors.wrappers.trial_hist_ev import TrialHistoryEvolution
from ngym_priors.wrappers.variable_mapping import VariableMapping
from ngym_priors.wrappers.time_out import TimeOut
from ngym_priors.wrappers.dynamic_noise import DynamicNoise
from ngym_priors.wrappers.monitor_extended import MonitorExtended
from ngym_priors.wrappers.catch_trials import CatchTrials
from ngym_priors.wrappers.trial_hist import TrialHistory
from ngym_priors.wrappers.combine import Combine
from ngym_priors.wrappers.identity import Identity
from ngym_priors.wrappers.transfer_learning import TransferLearning

ALL_WRAPPERS = {'DynamicNoise-v0':
                'ngym_priors.wrappers.dynamic_noise:DynamicNoise',
                'TrialHistoryEv-v0':
                    'ngym_priors.wrappers.trial_hist_ev:TrialHistoryEvolution',
                'VariableMapping-v0':
                    'ngym_priors.wrappers.trial_hist_ev:VariableMapping',
                'Variable_nch-v0':
                    'ngym_priors.wrappers.variable_nch:Variable_nch',
                'TimeOut-v0':
                    'ngym_priors.wrappers.time_out:TimeOut',
                'VariableReactionTime-v0':
                    'ngym_priors.wrappers.variable_reaction_time:VariableReactionTime',
                'MonitorExtended-v0':
                    'ngym_priors.wrappers.monitor_extended:MonitorExtended',
                'CatchTrials-v0': 'ngym_priors.wrappers.catch_trials:CatchTrials',
                'TrialHistory-v0': 'ngym_priors.wrappers.trial_hist:TrialHistory',
                'Combine-v0': 'ngym_priors.wrappers.combine:Combine',
                'Identity-v0': 'ngym_priors.wrappers.identity:Identity',
                'TransferLearning-v0':
                    'ngym_priors.wrappers.transfer_learning:TransferLearning',
                }
def all_wrappers():
    return sorted(list(ALL_WRAPPERS.keys()))
