#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:02:11 2019

@author: mariadelacorte
"""                    
import pyxel
import constants
from mario import Mario
from princess import Princess
from donkeyKong import DonkeyKong
from plat import Plat
from ladders import Ladder
from barrels import Barrels
from barrels import auxBarrel

import random #for the princess & random number 
#to see if the barrel falls through the stairs

class Board:
    
    #for throwing the barrels
    def throw (self):
       if (len(self.barrels))<10:
           barrels=Barrels(constants.BARREL_X, constants.BARREL_Y)
           self.barrels.append(barrels)
           
    #init method were we initialize all of our variables
    def __init__(self):
        
                            #FOR THE BOARD
                            
        pyxel.init(constants.WIDTH, constants.HEIGHT,
                   caption=constants.CAPTION)
        
                            #FOR MARIO
                            
        self.mario = Mario(constants.MARIO_INIT_X, constants.MARIO_INIT_Y,
                           constants.LIVES)
        
                            #FOR THE PRINCESS
                            
        self.princess = Princess(constants.PRINCESS_X, constants.PRINCESS_Y)
        
                            #FOR DONKEY KONG
                            
        self.donkeyKong = DonkeyKong(constants.DONKEY_INIT_X, constants.DONKEY_INIT_Y)
    
                            #FOR THE POSITIONS OF THE PLATFORMS
                                               
        #creating a tupple with all the different possitions
        #platform were we want it to be
        self.plat = (Plat(0,226),Plat(0,191),
                     Plat(35,156),Plat(0,121),
                     Plat(35,86),Plat(0,51),
                     Plat(60,16))
      
                            #FOR POSITIONS OF THE LADDERS
                            
        self.ladder = (Ladder(200,191), 
                       Ladder(50,156),Ladder(157,156),
                       Ladder(200,121),
                       Ladder(42,86),Ladder(132,86),
                       Ladder(200,51),
                       Ladder(100,16))
           
                            #FOR THE NON WORKING LADDERS
                            
        self.Nonladder = (Ladder(87,199),  Ladder(87,218),
                          Ladder(76,129), Ladder(76,148),
                          Ladder(80,59), Ladder(80,78))
        
                            #FOR THE BARRELS_STACK
                            
        self.stack = Barrels(constants.BARREL_STACK_X, constants.BARREL_STACK_Y)
        
        
                            #FOR THE BARRELS
                            
        #creating a barrels liste
        self.barrels=[]
        #we create a list of barrels because we are going to be able to throw 
        #more than one barrel. 
        self.barrels=Barrels(constants.BARREL_X, constants.BARREL_Y)
        self.barrels=[]
        
        #auxiliar for being able to eliminate barrels based on their position
        self.aux = auxBarrel()
        
        #Loading the pyxres file
        pyxel.load("assets/gameboard.pyxres")
        
        #To start the game we invoke the run method with the update and 
        #draw functions
    
        pyxel.run(self.update, self.draw)
        
        

    # To use pyxel we need to define two functions, one will do all the
    # calculations needed each frame, the other will paint things on the screen
    # They can have any name, but the 'standard' ones are update and draw
    
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
            
        #if mario has more than 3 lives and is not at the platform of the princess
        if(self.mario.lives>0 and self.mario.withPrincess==False): 
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.mario.image= constants.MARIO_IMAGE #inserting mario looking right
                self.mario.climb(self.ladder,"right") #
                #to know if its or not climbing 
                if(self.mario.climbing==False):
                    self.mario.move("right")
                else:
                    self.mario.move("dont")
                        
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.mario.image= constants.MARIO_IMAGE_L #inserting mario looking left
                self.mario.climb(self.ladder,"left")
                #to know if its or not climbing 
                if(self.mario.climbing==False):
                    self.mario.move("left")
                else:
                    self.mario.move("dont")
            
            elif pyxel.btn(pyxel.KEY_UP):
                self.mario.image= constants.MARIO_IMAGE_C
                self.mario.climb(self.ladder,"up")
                if(self.mario.climbing==True):
                    self.mario.move("up")
                else:
                    self.mario.move("dont")
               
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.mario.image= constants.MARIO_IMAGE_C
                self.mario.climb(self.ladder,"down")
                if(self.mario.climbing==True):
                    self.mario.move("down")
                else:
                    self.mario.move("dont")
                    
            if pyxel.btn(pyxel.KEY_SPACE):
                if(self.mario.canJump==True):
                    self.mario.jumping=True
                else:
                    self.mario.move("dont")
                    
                        
                                    #PRINCESS
                                    
            #Random shouting from the princess                        
            self.princess.shouting()
            
                
                
                                     #MARIO
                                     
            #to know if mario is at a platform                         
            self.mario.atPlat(self.plat)
            #to know if mario is at the Princess platform
            self.mario.atPrincess(self.plat[6])       
            
                                    #JUMPING
            if self.mario.jumping:
                self.mario.jump() 
                        
            #falling when not JUMPING and Not at a platform
            if (self.mario.jumping == False and self.mario.inPlat == False 
                and self.mario.climbing==False):
                self.mario.gravity() #gravity working
            #to know wether mario can jump, if mario is not jumping & on a platform
            #Mario can jump
            if(self.mario.jumping==False and self.mario.inPlat==True):
                self.mario.canJump=True
            
                                    #BARRELS  
            
            #creating a random number for when the barrel is being thrown
            number = random.randint(60,190)
            
            if pyxel.frame_count % number ==0: #The barrel will get out of the stack
                #whenever the position of x = 150
                self.donkeyKong.image=constants.DONKEY_IMAGE_R
                self.throw()
            for barr in range (len(self.barrels)):
                    #Checking if the barel is at the platform
                self.barrels[barr].atPlat(self.plat) 
                #to put the desired direction
                self.barrels[barr].directionAfterFall(self.plat)
                #to know if its at a ladder
                self.barrels[barr].atLadder(self.ladder)
                
                                #BARREL MOVEMENT NOT FALLING INTO THE LADDER
                            
                if self.barrels[barr].inLadder==False:
                
                    #if the barrels are at the platform they will move
                    if(self.barrels[barr].inPlat==True):
                        self.barrels[barr].move(self.barrels[barr].movement)
                        
                    #activating the gravity if its not at a platform
                    if(self.barrels[barr].inPlat==False): 
                        self.barrels[barr].gravity()
                    
                    #if the barrel is at the last platform, and in x<30 we´ll eliminate it 
                    if(self.barrels[barr].x < 30 and self.barrels[barr].y ==216 ):
                        self.aux.eliminate=True
                        self.aux.pos=barr #To know the position when its being eliminated
                            
                                    #BARREL MOVEMENT FALLING INTO THE LADDER
                                    
                if (self.barrels[barr].inLadder==True):
                    self.barrels[barr].gravityForLadder()
                    
                                    #MARIO JUMPING A BARREL
                                    
                if(self.mario.jumping==True  
                   and self.mario.x in range (self.barrels[barr].x-10,self.barrels[barr].x + 10)
                   and self.mario.y in range (self.barrels[barr].y-35, self.barrels[barr].y)):
                   self.mario.canScore=True
                    
                                   #MARIO BEING HITTED BY A BARREL
                                   
                self.mario.beingHitted (self.barrels, barr)                  
            
                        
            #for eliminating a barrel out of the list
            if(self.aux.eliminate==True and self.barrels[self.aux.pos].x < 1
               and self.barrels[self.aux.pos].y ==216 
               and self.mario.gameOver==False and self.mario.won==False):
                self.barrels.remove(self.barrels[self.aux.pos])
            
            #taking one live from mario
            if (self.mario.hitted==True):
                for barr in range (len(self.barrels)):
                    if(barr<len(self.barrels)):
                        self.barrels.remove(self.barrels[barr])
                self.mario.lostLife()
                self.mario.score=0
            
            #restoring being hitted to false
            self.mario.hitted=False
          
            
        #if player has reached the princess platform  "YOU WON"              
        if(self.mario.withPrincess==True and self.mario.lives>0):
            self.mario.won=True
        
        #if player has lost all of his lives "GAME OVER"       
        if(self.mario.lives==0):
            self.mario.gameOver=True 
       
        #If the player presses "enter" they want to play again, therefore all
        #the values are restored
        if pyxel.btn(pyxel.KEY_ENTER):
            #removing all of the barrels from the board
            self.mario.gameOver = False 
            self.mario.won = False 
            self.mario.withPrincess=False
            
            for barr in range (len(self.barrels)):
                if(barr<len(self.barrels)):
                    self.barrels.remove(self.barrels[barr])
                    
            self.mario.x = constants.MARIO_INIT_X
            self.mario.y = constants.MARIO_INIT_Y
            #restoring initial values
            self.mario.lives = 3
            self.mario.score = 0
            
            
    def draw(self):
        #el fondo sera negro
        pyxel.cls(0)
        
        #BEST WAY: we use * to unpack the tuple 
        #each element of the  tuple is copied into a parameter
                                #INSERT ON THE BOARD
                                
        pyxel.blt(self.princess.x, self.princess.y, *self.princess.image)

                                #INSERT DONKEY KONG ON THE BOARD
                                
        pyxel.blt(self.donkeyKong.x, self.donkeyKong.y, *self.donkeyKong.image)
        
                                #INSERT PLATFORMS ON THE BOARD
        count=0
        for platform in self.plat:
            if(count==0 or count == 2 or count == 4):
                pyxel.blt(platform.x, platform.y, *platform.image, colkey=0)
            #†his platforms have a hole on the right
            elif(count==1 or count==3 or count==5):
                pyxel.blt(platform.x, platform.y, *platform.image2, colkey=0)
            #special Platform for the princess
            else:
                pyxel.blt(platform.x, platform.y, *platform.imagePrincess, colkey=0)
            count+=1
            
                            #INSERT LADDERS ON THE BOARD
        
        #Going 
        for ladd in self.ladder:
            pyxel.blt(ladd.x, ladd.y, *ladd.image, colkey=0)
            
        count=0
        for nonLadd in self.Nonladder:
                pyxel.blt(nonLadd.x, nonLadd.y, *nonLadd.imageUp, colkey=0)
                
        #INSERT MARIO ON THE BOARD
                            
        pyxel.blt(self.mario.x, self.mario.y, *self.mario.image, colkey=0)
        
    
                            #INSERT BARRELS_STACK ON THE BOARD
                            
        pyxel.blt(constants.BARREL_STACK_X, constants.BARREL_STACK_Y, *self.stack.imageStack, colkey=0)
        
                            #INSERT BARREL ON THE BOARD
                            
        pyxel.blt(constants.BARREL_X, constants.BARREL_Y, *constants.BARREL_R, colkey=0)
        for barr in self.barrels:
            pyxel.blt( barr.x, barr.y, *barr.imageTurn, colkey=0)
            
        #Printing on Screen the actual score of the player 
        pyxel.text(210, 2, ("SCORE"),7)
        pyxel.text(215,10,str(self.mario.score),pyxel.frame_count % 16) 
        
        #Printing on Screen the remaining lives of the player 
        pyxel.text(235, 2, ("LIVES"),7)
        pyxel.text(243,10,str(self.mario.lives),11)
        
        #IF THE GAME IS OVER IT WILL APPEAR THE IMAGE OF "GAME OVER"
        #IN THE MIDDLE OF THE SCREEN
        if (self.mario.gameOver==True):
            pyxel.blt(constants.LOST_X,constants.LOST_Y,*constants.LOST,colkey=0)
            #If the user wants to play again
            pyxel.text(100, 205, ("To play again press Enter"),7)
            #If the user wants to exit the game 
            pyxel.text(100, 215, ("To exit the game press Q"),8)
            
        #IF THE PLAYER HAS WON IT WILL APPEAR THE IMAGE OF "YOU WON"
        #IN THE MIDDLE OF THE SCREEN
        if(self.mario.won==True):
            pyxel.blt(constants.WON_X,constants.WON_Y,*constants.WON,colkey=0)
            #If the user wants to play again
            pyxel.text(100, 205, ("To play again press Enter"),7)
            #If the user wants to exit the game
            pyxel.text(100, 215, ("To exit the game press Q"),8)
            
        
Board()
    
      #    python3 Desktop/pyxelExamples/donkeyKong/board.py
