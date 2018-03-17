# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:25:30 2018

@author: Thomas Marks
"""
from math import sqrt
from math import arctan
from math import pi
from enum import Enum
class GPSCoord:
    def __init__(self, MMC):
        self.number = MMC[0]
        self.x = MMC[1]
        self.y = MMC[2]
        self.z = MMC[3]
        self.timeStamp = MMC[4]
    def __lt__(self, other):
        return self.timeStamp < other.timeStamp
    def __eq__(self, other):
        return self.timeStamp == other.timeStamp
    def __mul__(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
    def __pow__(self, other):
        return [(self * other) / abs(self.timeStamp - other.timeStamp), abs(self.timeStamp - other.timeStamp)]

class Section(Enum):
    TOP : 1
    RIGHT : 2
    BOT : 3
    LEFT : 4

class Track:
    def __init__(self, lane, GPSQueue, SendQueue):
        self.GPSQueue = GPSQueue
        self.SendQueue = SendQueue
        self.straight = 84.39
        self.trackWidth = 1.22
        self.innerRadius = 36.50 + self.trackWidth * (lane - 1)
        self.outterRadius = self.innerRadius + self.trackWidth
        self.topOfTop = - self.trackWidth * lane
        self.botOfTop = -self.trackWidth * (lane - 1)
        self.topOfBot = 73 * self.trackWidth * (lane - 1)
        self.botOfBot = self.topOfBot + self.trackWidth
    def update(self):
        while True:
            currentGPS = self.GPSQueue.get()
            if(currentGPS == "Quit"):
                self.SendQueue.add("Quit")
                break
            else:
                self.__updateSelf(currentGPS)
                
                
                
                
    def __updateSelf(self, GPS):
        #TODO implement the change
        return 0
    
    #Determines what section of the track the user is in
    def sectionGetter(self, coord):
        x = coord.x
        y = coord.y
        if(x > 0 and x < self.straight):
            if(y < self.innerRadius):
                return Section.TOP
            else:
                return Section.BOT
        if x < 0:
            return Section.LEFT
        else:
            return Section.RIGHT
                
                
                
                
                


#Determines if the user is in the lane (if not most powerful buzz is used)
def sectionChecker(coord, section, track):
    x = coord.x
    y = coord.y
    if(section is Section.TOP):
        if(y < track.topOfTop and y > track.botOfTop):
            return True
        else:
            return False
    elif(section is Section.BOT):
        if(y > track.topOfBot and y < track.botOfBot):
            return True
        else:
            return False
    #TODO Make the other cases
    #
    return None

#Used to make sure the correct angle is returned from the two coordinates passed
def bearingFinder(coord1, coord2):
    x1 = coord1.x
    x2 = coord2.x
    y1 = coord1.y
    y2 = coord2.y
    if(x2 > x1):
        return arctan((y2 - y1)/(x2 - x1))
    else:
        return arctan((y2 - y1)/(x2 - x1)) - pi
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    