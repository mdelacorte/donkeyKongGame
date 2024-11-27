#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:01:40 2019

@author: mariadelacorte
"""

#(0(imagebank), 48(Donde empieza x), 0 (Donde empieza y ), 16(ancho) , 16(altura)) 
        
            

#asigning the size of the board
WIDTH = 256
HEIGHT = 240

#header information   
CAPTION = "DONKEY KONG"

#YOU WON AT THE END OF THE GAME
WON_X=100
WON_Y=100
WON=(2,0,46,64,45)
#YOU LOST AT THE END OF THE GAME
LOST_X=100
LOST_Y=100
LOST=(2,0,0,64,42)


#CARACTERS IN DONKEY KONG

                        #Mario information
MARIO_INIT_X = 0
MARIO_INIT_Y = 210 #210

MARIO_SIZE = 16
LIVES = 3
#When going to the right
MARIO_IMAGE = (0,0,0,12,16)
#When going to the left
MARIO_IMAGE_L = (0,16,0,16,16)
#When jumping LEFT
MARIO_IMAGE_JL = (0,32,0,16,16)
#When jumping RIGHT
MARIO_IMAGE_JR = (0,48,0,16,16)
#When climbing
MARIO_IMAGE_C = (0,64,0,16,16)

                        #Donkey Kong Information
                        

DONKEY_INIT_X = 25
DONKEY_INIT_Y = 19

#When front
DONKEY_IMAGE_F = (0,0,16,24,32)
#When going to the left
DONKEY_IMAGE_L = (0,24,16,24,32)
#When going to the right
DONKEY_IMAGE_R = (0,56,16,24,32)
#donkey standing
DONKEY_IMAGE_S = (0,56,16,24,32)



                        #Princess Information

PRINCESS_X = 60
PRINCESS_Y = 2
                        
PRINCESS_IMAGE = (0,0,48,16,20)
PRINCESS_IMAGE_SHOUT = (0,16,48,39,20)




#OBJECTS IN DONKEY KONG

                        #Ladders information


LADDER_IMAGE = (1,0,64,10,35)
LADDER_IMAGE_UP = (1,0,64,10,8)
LADDER_IMAGE_PRINCESS = (1,0,64,10,30)


                        #Barrels information

BARREL_STACK_X = 1
BARREL_STACK_Y = 21
BARREL_SIZE = 10

BARREL_X=32
BARREL_Y=40  

BARREL_STACK = (1,0,0,22,30)
BARREL_R = (1,24,0,10,10)
BARREL_L = (1,40,0,15,15)
BARREL_SIDE = (1,24,18,15,10) 


                        #Platform information

PLATFORM_IMAGE1 = (1,0,48,255,8) #bottom platform
PLATFOM_IMAGER  = (1,0,48,220,8) # Right hole
PLATFORM_IMAGE2 = (1,0, 48, 60, 8) #platform for the princess
