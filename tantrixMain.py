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


TANTRIXC = (["r", "y", "y", "b", "r", "b"],
            ["b", "y", "y", "b", "r", "r"],
            ["y", "r", "r", "b", "b", "y"],
            ["b", "y", "r", "b", "r", "y"],
            ["r", "y", "y", "r", "b", "b"],
            ["y", "r", "b", "y", "b", "r"],
            ["r", "b", "b", "y", "r", "y"],
            ["y", "b", "b", "r", "y", "r"],
            ["r", "y", "b", "r", "b", "y"],
            ["b", "y", "y", "r", "b", "r"],
            ["y", "r", "r", "b", "y", "b"],
            ["b", "r", "r", "y", "b", "y"],
            ["y", "b", "b", "y", "r", "r"],
            ["r", "y", "y", "b", "b", "r"],
            ["r", "g", "g", "r", "y", "y"],
            ["y", "g", "g", "y", "r", "r"])

class TantrixEngine(search.Problem):
    initial = []
    tiles = []
    tileFilter = []
    
    def __init__(self,initial):
        self.initial = initial

    def actions(self, state):
        actions = ["rotate"]
        
        return tuple(actions)
        
    def result(self, state, action):
        return state
        
    def goal_test(self,state):
        return True
        
    def attachNeighbours(self,tileIndex):
        prevLine = -1
        thisLine = 0
        nextLine = 1
        prevCount = 0
        thisCount = 1
        nextCount = 2
        tileCount = len(self.tiles)
        
        #find the line of our tile, not enough time to make it simpler
        while tileIndex < thisLine or tileIndex > (thisLine + (thisCount - 1)):
            prevLine = thisLine
            prevCount = thisCount
            thisLine = nextLine
            thisCount = nextCount
            nextLine = thisLine + thisCount
            nextCount = nextCount + 1
            
        position = tileIndex - thisLine
        if(prevLine != -1):
            if(position > 0):
                self.tiles[tileIndex].setNeighbour(self.tiles[prevLine + position - 1], 5)
            if(position < thisCount - 1):
                self.tiles[tileIndex].setNeighbour(self.tiles[prevLine + position], 0)
            
        if(position > 0):
            self.tiles[tileIndex].setNeighbour(self.tiles[tileIndex - 1], 4)
        if(position < thisCount - 1):
            self.tiles[tileIndex].setNeighbour(self.tiles[tileIndex + 1], 1)
            
        if(nextLine < tileCount):
            self.tiles[tileIndex].setNeighbour(self.tiles[nextLine + position], 3)
            self.tiles[tileIndex].setNeighbour(self.tiles[nextLine + position + 1], 2)
            
        
        
        return tileIndex
        
    def addTile(self,newTile):
        self.tiles.append(newTile)
        
    def readyStruct(self):
        tileCount = len(self.tiles)
        
        for i in range(tileCount):
            self.initial.append(i)
            
    def printState(self):
        result = ""
        for i in range(len(self.initial)):
            result = result + str(self.initial[i]) + " "
        return result
        
    def printNeighbours(self):
        result = ""
        
        for i in range(len(self.tiles)):
            result = result + self.tiles[i].printNeighbours() + "\n"
        return result
        
    def printSignatures(self):
        result = ""
        
        for i in range(len(self.tiles)):
            result = result + self.tiles[i].printSignature() + "\n"
        return result
        
    def attachAllNeighbours(self):
        for i in range(len(self.tiles)):
            self.attachNeighbours(i)
        
        

engine = TantrixEngine([])


for i in range(6):
    engine.addTile(Tile.Tile(TANTRIXC[i],i+1))


engine.readyStruct()

engine.attachAllNeighbours()
print("we are ready")
print(engine.printNeighbours())
print(engine.printSignatures())
print(engine.printState())

print(Tile.TILE_SIDES)
print("cyka blyat")
