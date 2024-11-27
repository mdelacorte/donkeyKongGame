#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:56:10 2019

@author: mariadelacorte
"""
import constants
import random

class Barrels:
    
    def __init__(self,x,y):
        if x>=0:
            self.x=x
        else:
            self.x=0
        if y>=0:
            self.y=y
        else:
            self.y=0
            
        self.imageStack = constants.BARREL_STACK
        self.imageTurn = constants.BARREL_R
        self.movement="right"
        self.sideImage=constants.BARREL_SIDE
        
        self.inLadder=False
        self.eliminate=False
        self.inPlat=False
        
    
    #movement of the barrel    
    def move(self, movem:str): 
        if movem == "right":#will move the barrel to the right
            self.x=self.x + 1
        if movem == "left":#will move the barrel to the left
            self.x=self.x - 1    
            
    #to know if our barrel is at a ladder
    def atLadder (self,lade): 
        inLadder = False
        #random number it will only be true when the rand number=1
        number=random.randint(1,4)
        if number==1:
            for lad in range(len(lade)):
                if(((self.x in range(lade[lad].x - 6, lade[lad].x + 6)) 
                and (self.y in range(lade[lad].y-16, lade[lad].y +19)))):
                    number=random.randint(1,4) #probability 25%
                    if number==1:
                        inLadder = True
        self.inLadder = inLadder
           
    #checking if the barrel is at a platform    
    def atPlat(self,plat): 
       inAnyPlat=False
       for platf in range(len(plat)):
           
          if (self.y  == plat[platf].y - constants.BARREL_SIZE):
              inAnyPlat=True #my Barrel is at a platform
              
          if ((platf == 1 or platf ==3 or platf ==5) and self.x > 212  
              and self.y  == plat[platf].y - constants.BARREL_SIZE):
              inAnyPlat=False #my Barrel isnt at a platform
              
          if ((platf == 2 or platf ==4) and self.x < 35  and self.y  == plat[platf].y - constants.BARREL_SIZE):
              inAnyPlat=False #my Barrel isnt at a platform
        
              
       self.inPlat = inAnyPlat  
    
    #this will be the direction after our barrel has falled from the platform hole
    def directionAfterFall (self, plat):
        for platf in range(len(plat)):
            if ((platf == 1 or platf ==3 or platf ==5) 
                and self.y == plat[platf].y - constants.BARREL_SIZE):
                self.movement= "right"
            if ((platf==0 or platf == 2 or platf ==4 ) 
                and self.y == plat[platf].y - constants.BARREL_SIZE):
                self.movement="left"
            
    #gravity for when its falling through a platform hole    
    def gravity(self):
        self.move(self.movement)
        self.y = self.y + 1
        
    #gravity for when its falling from a ladder    
    def gravityForLadder(self):
        self.y = self.y + 1

            
#auxiliar         
class auxBarrel:
    
    def __init__(self):
        
        #if we have to eliminate that barrel
        self.eliminate=False
        #position of the barrel we want to eliminate
        self.pos=1
        self.randomThrow = 0
        
        
        
    
       
        
