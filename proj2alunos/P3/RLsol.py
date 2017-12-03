# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
import numpy as np

def max(Q, state):
    numberActions = len(Q[state])
    maxReward = -1
    for i in range(numberActions):
        if Q[state][i] > maxReward:
            maxReward = Q[state][i]
    return maxReward

def Q2pol(Q, eta=5):
    return np.exp(eta*Q)/np.dot(np.exp(eta*Q), np.array([[1,1],[1,1]]))
	
class myRL:

    def __init__(self, nS, nA, gamma):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((nS,nA))
        
    def traces2Q(self, trace):
        self.Q = np.zeros((self.nS,self.nA))
        newQ = np.zeros((self.nS,self.nA))
        secondGamma  = 0.01
        while True:            
            for line in trace: #each line contains:[initialState, action, finalState, reward]
    
                initialState = int(line[0])
                action = int(line[1])
                finalState = int(line[2])
                reward = line[3]
                
                newQ[initialState,action] = newQ[initialState,action] + secondGamma * (reward + self.gamma * max(newQ,finalState) - newQ[initialState,action])
                
            err = np.linalg.norm(self.Q-newQ)
            self.Q = np.copy(newQ)
            if err<1e-10:
                break 
        return self.Q



            