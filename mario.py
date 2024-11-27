#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:01:27 2019

@author: mariadelacorte
"""
import constants
class Mario:
    #checking that the initial position is correct
    def __init__(self,x,y,lives):
        if x>=0:
            self.x=x
        else:
            self.x=0
        if y>=0:
            self.y=y
        else:
            self.y=0
            
        if lives>0:
            self.lives=lives
        else:
            self.lives = 3
         
            
        self.prueba=False   
        self.prueba2=False 
        self.atPLatfor=False
        self.count=0
        self.lives=lives
        self.score=0
        
        self.scor=False
        self.canScore=False
        self.hitted = False
        
        self.gameOver = False
        self.won=False
        
        self.jumping= False
        self.falling=False
        self.climbing= False
        self.canJump=True
        
        self.withPrincess= False
        self.inPlat=True
        
        self.image= constants.MARIO_IMAGE
                
    #method for the movement of mario            
    def move(self,string:str):
     
        if string == "right":
            #if you are at the limit x position (on the right)
            #you can only move to the right  
            if self.x>=0 and self.x<243:
                self.x = self.x + 1
            
            
            if self.x<=0: 
                self.x = self.x + 1
         
        elif string == "left":
            #if you are at the limit x position  (on the left)
            #you can only move to the left  
            if self.x>0 and self.x<243:
                self.x = self.x - 1 
            if self.x>=243: 
                self.x = self.x - 1
        
        elif string == "up":
                self.y = self.y - 1   
        elif string ==  "down":
                self.y = self.y + 1
        else:
            self.x=self.x
            self.y=self.y
            
    #if mario has lost a live -1        
    def lostLife (self):
        self.lives = self.lives -1
        
    #if mario has jumped over a barrel    
    def scoring(self):
        if(self.canScore==True):
            self.score = self.score + self.canScore
    
    #to check if mario is in the position for climbing a ladder        
    def climb(self,lade,movement): 
        climbing=False
        for lad in range(len(lade)):
            if(movement=="up" and ((self.x in range(lade[lad].x - 6, lade[lad].x + 6)) 
            and (self.y in range(lade[lad].y-15, lade[lad].y +20)))):
                climbing=True
            if(movement=="down" and ((self.x in range(lade[lad].x - 6, lade[lad].x + 6)) 
            and (self.y in range(lade[lad].y-16, lade[lad].y +19)))):
                climbing=True
        self.climbing= climbing
        
    #to check if mario is at a flatform
    def atPlat(self,plat): 
       inAnyPlat=False
       for platf in range(len(plat)):
          if (self.y  == plat[platf].y - constants.MARIO_SIZE):
              inAnyPlat=True
          if ((platf == 1 or platf ==3 or platf == 5) and self.x > 220  and self.y  == plat[platf].y - constants.MARIO_SIZE):
              inAnyPlat=False
          if ((platf == 2 or platf ==4 or platf ==4 ) and self.x < 30  and self.y  == plat[platf].y - constants.MARIO_SIZE):
              inAnyPlat=False
              
       self.inPlat = inAnyPlat  
    #to check if mario is at the Princess Platform   
    def atPrincess(self, plat):
        princess=False
        if (self.y  == plat.y - constants.MARIO_SIZE):
                princess=True
              
        self.withPrincess=princess
        
    #for the jump of mario    
    def jump(self): 
        
        if self.count < 13 :
            self.y = self.y - 1
            self.count += 1
            self.canJump=False
            
        else:
            self.count=0
            self.jumping=False #ya no esta saltando
            self.falling=True
            
            #only if mario is not jumping and can Score=True mario will gain
            #100 points
            if(self.canScore==True):
                self.score=self.score + 100
            #restoring the value to false
            self.canScore=False
            
    def gravity(self): #GRAVITY FOR MARIO
        self.y = self.y + 1
             
        
    def beingHitted(self, barrels, barr):
        if (self.x in range (barrels[barr].x-12, barrels[barr].x+12)
        and self.y in range (barrels[barr].y-10, barrels[barr].y)):
            self.x=constants.MARIO_INIT_X #INSERTING MARIO AT THE INITIAL POSITION
            self.y=constants.MARIO_INIT_Y #INSERTING MARIO AT THE INITIAL POSITION
            #assigning hitted=True, so that we can take out 1 life from mario
            self.hitted=True     
        
        
        
        
           
     
            
            
            
            
            

         
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
