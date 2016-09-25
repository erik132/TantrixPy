# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:45:20 2016

@author: Erik
"""
import search


class TantrixEngine(search.Problem):
    initial = []
    
    def __init__(self,initial,wildcard1):
        self.initial = initial

    def actions(self, state):
        actions = ["rotate"]
        
        return tuple(actions)
        
    def result(self, state, action):
        return state
        
    def goal_test(self,state):
        return True




t = 0

print(t)