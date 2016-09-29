# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:22:29 2016

@author: Erik
"""

TILE_SIDES = 6
HALF_TILE = 3

class Tile():
    colors = [] #keep in mind, this is static until overwrite from __init__
    neighbours = None
    id = 0
    
    
    
    def __init__(self, colors, id):
        self.colors = colors
        self.id = id
        self.neighbours = []
        for i in range(TILE_SIDES):
            self.neighbours.append(None)
        
        
    def rotateRight(self):
        tempColor = self.colors[TILE_SIDES - 1]
        for i in range(0,TILE_SIDES - 1):
            self.colors[TILE_SIDES - 1 - i] = self.colors[TILE_SIDES - 2 - i]
        self.colors[0] = tempColor
    

    def printSignature(self):
        return "" + str(self.colors) + " " + str(self.id)
        
    def printNeighbours(self):
        result = str(self.getId()) + " of "
        
        for i in range(TILE_SIDES):
            if(self.neighbours[i] == None):
                result = result + "none "
            else:
                result = result + str(self.neighbours[i].getId()) + " "
        return result
        
    def resetNeighbours(self):
        for i in range(0,TILE_SIDES):
            self.neighbours[i] = None

    def setNeighbour(self,neighbour,index):
        self.neighbours[index] = neighbour

    def getNeighbour(self,index):
        return self.neighbours[index]
        
    def setId(self, id):
        self.id = id
        
    def getId(self):
        return self.id
        
        
    def alignTo0(self):
        color0 = ''
        side = 0
        if(self.neighbours[0] != None):
            color0 = self.neighbours[0].getNeighbourColor(0)
            side = 0
            
        else:
            color0 = self.neighbours[5].getNeighbourColor(5)
            side = 5
            
        tries = 0
        self.rotateRight()
        tries = tries + 1
        while(color0 != self.colors[side]):
            self.rotateRight()
            tries = tries + 1
            if(tries > TILE_SIDES):
                return False
        return True
        
    def getNeighbourColor(self,nSide):
        nSide = nSide + HALF_TILE
        if(nSide > (TILE_SIDES - 1)):
            nSide = nSide - TILE_SIDES
        return self.colors[nSide]

    def checkUpperColors(self):
        colorOther = ""
        
        for i in range(4,TILE_SIDES):
            if(self.neighbours[i] == None):
                continue
            colorOther = self.neighbours[i].getNeighbourColor(i)
            if(colorOther != self.colors[i]):
                return False
        
        return True
        


