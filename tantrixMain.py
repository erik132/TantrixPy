# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:45:20 2016

@author: Erik
"""

import sys

i1 = "C:\\machine learning\\aimapy\\TantrixPy" in  sys.path
print(i1)
if(i1 == False):
    sys.path.append("C:\\machine learning\\aimapy\\TantrixPy")

import search
import Tile


TANTRIX01 = ["r", "y", "y", "b", "r", "b"]
TANTRIX02 = ["b", "y", "y", "b", "r", "r"]
TANTRIX03 = ["y", "r", "r", "b", "b", "y"]
TANTRIX04 = ["b", "y", "r", "b", "r", "y"]
TANTRIX05 = ["r", "y", "y", "r", "b", "b"]
TANTRIX06 = ["y", "r", "b", "y", "b", "r"]
TANTRIX07 = ["r", "b", "b", "y", "r", "y"]
TANTRIX08 = ["y", "b", "b", "r", "y", "r"]
TANTRIX09 = ["r", "y", "b", "r", "b", "y"]
TANTRIX10 = ["b", "y", "y", "r", "b", "r"]
TANTRIX11 = ["y", "r", "r", "b", "y", "b"]
TANTRIX12 = ["b", "r", "r", "y", "b", "y"]
TANTRIX13 = ["y", "b", "b", "y", "r", "r"]
TANTRIX14 = ["r", "y", "y", "b", "b", "r"]
TANTRIX15 = ["r", "g", "g", "r", "y", "y"]
TANTRIX16 = ["y", "g", "g", "y", "r", "r"]

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
        
    def attachNeighbours(self,tileIndex):
        return tileIndex
        


        
print("cyka blyat")
print(TANTRIX01)
t = 99999

print(t)