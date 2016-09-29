# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:45:20 2016

@author: Erik
"""

import sys
import itertools

tantrixPath = "C:\\machine learning\\aimapy\\TantrixPy"
i1 = tantrixPath in  sys.path
print(i1)
if(i1 == False):
    sys.path.append(tantrixPath)

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
    initial = tuple([]) #pointer array where each element points to an element in tile array
    tiles = []
    
    def __init__(self,initial):
        self.initial = tuple(initial)

    def actions(self, state):
        actions = []
        tileCount = len(self.tiles)
        lineLimit = 1;
        lineCurrent = 0;
        
        for i in range(tileCount):
            if((i in state) == False):
                actions.append(str(i))
            else:
                lineCurrent = lineCurrent + 1
                if(lineLimit == lineCurrent):
                    lineCurrent = 0
                    lineLimit = lineLimit + 1
        if(lineCurrent == 0 and (-1 in state)):
            if(self.testPermut(list(state),state.index(-1) - 1) == False):
                return tuple([])
            
        
        return tuple(actions)
        
    def result(self, state, action):
        state2 = list(state)
        vacantSlot = state2.index(-1)
        state2[vacantSlot] = int(action)
        
        return tuple(state2)
        
    def goal_test(self,state):
        state2 = list(state)
        if(-1 in state2):
            return False
        else:
            if(self.testPermut(state2,len(self.tiles) - 1)):
                print(self.printSignatures(state2))
                return True
            else:
                return False
                
    def value(self,state):
        state2 = list(state)
        vacantSlot = state2.index(-1)
        return vacantSlot
        
    def testPermut(self,state,toIndex):
        result = False
        if(toIndex <= 0):
            return True
            
        self.detachAllNeighbours()
        self.attachNeighbours(toIndex,state)
        
        
        for i in range(Tile.TILE_SIDES):
            self.tiles[state[0]].rotateRight()
            result = self.testRec(1,state, toIndex)
            if(result):
                break
            
        return result
        
        
    def testRec(self,index,state, toIndex):
        tile1 = self.tiles[state[index]]
        result = False
        
        for i in range(2):
            if(not tile1.alignTo0()):
                break
            
            if(tile1.checkUpperColors()):
                if(index < toIndex):
                    result = self.testRec(index + 1, state,toIndex)
                    if(result):
                        return result
                else:
                    return True
        return result
        
        
    #tileIndex is misleading, as it is the element number in the pointer array.
    def attachNeighbours(self,toIndex, state):
        prevLine = -1
        thisLine = 0
        nextLine = 1
        prevCount = 0
        thisCount = 1
        nextCount = 2
        tileCount = len(self.tiles)
        tempPos = -1
        #print("to index " + str(toIndex) + " " + str(state))
            
        for tileIndex in range(toIndex + 1):
            if(state[tileIndex] == -1):
                break
            if(tileIndex > (thisLine + (thisCount - 1)) ):
                prevLine = thisLine
                prevCount = thisCount
                thisLine = nextLine
                thisCount = nextCount
                nextLine = thisLine + thisCount
                nextCount = nextCount + 1
            
            
            position = tileIndex - thisLine
            if(prevLine != -1):
                if(position > 0):
                    tempPos = state[prevLine + position - 1]
                    self.tiles[state[tileIndex]].setNeighbour(self.tiles[tempPos], 5)
                        
                if(position < thisCount - 1):
                    tempPos = state[prevLine + position]
                    self.tiles[state[tileIndex]].setNeighbour(self.tiles[tempPos], 0)
                
            if(position > 0):
                tempPos = state[tileIndex - 1]
                self.tiles[state[tileIndex]].setNeighbour(self.tiles[tempPos], 4)
            if(position < thisCount - 1):
                tempPos = state[tileIndex + 1]
                if(tempPos != -1):
                    self.tiles[state[tileIndex]].setNeighbour(self.tiles[tempPos], 1)
                
            if(nextLine < tileCount):
                tempPos = state[nextLine + position]
                if(tempPos != -1):
                    self.tiles[state[tileIndex]].setNeighbour(self.tiles[tempPos], 3)
                
                tempPos = state[nextLine + position + 1]
                if(tempPos != -1):
                    self.tiles[state[tileIndex]].setNeighbour(self.tiles[tempPos], 2)
            
        
    def addTile(self,newTile):
        self.tiles.append(newTile)
        
    def readyStruct(self):
        tileCount = len(self.tiles)
        
            
            
    def printState(self,state):
        result = ""
        for i in range(len(self.tiles)):
            if(state[i] == -1):
                break
            result = result + str(self.tiles[state[i]].getId()) + " "
        return result
        
    def printNeighbours(self):
        result = ""
        
        for i in range(len(self.tiles)):
            result = result + self.tiles[i].printNeighbours() + "\n"
        return result
        
    def printSignatures(self,state):
        result = ""
        
        for i in range(len(self.tiles)):
            if(state[i] == -1):
                break
            result = result + self.tiles[state[i]].printSignature() + "\n"
        return result
        
    def attachAllNeighbours(self,state):
        self.attachNeighbours(len(self.tiles)-1,state)
            
    def detachAllNeighbours(self):
        for i in range(len(self.tiles)):
            self.tiles[i].resetNeighbours()
        
        
            
def brutalForce(tant):
    initList = []
    for i in range(len(tant.initial)):
        initList.append(i)
    
    
    permGen = itertools.permutations(initList)
    for perm in permGen:
        if(tant.goal_test(perm)):
            break
        
            
tileAmount = 15
order = []
for i in range(tileAmount):
    order.append(-1)

engine = TantrixEngine(order)


for i in range(tileAmount):
    engine.addTile(Tile.Tile(TANTRIXC[i],i+1))


engine.readyStruct()

print("search start")
#brutalForce(engine)
#search.breadth_first_search(engine)
#search.depth_limited_search(engine,15)
search.depth_first_graph_search(engine)
print("search end")

