#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:05:14 2019

@author: mariadelacorte
"""
import constants
import random

class Princess:
    #checking that the initial position is correct
    def __init__(self,x,y):
        if x>=0:
            self.x=x
        else:
            self.x=0
        if y>=0:
            self.y=y
        else:
            self.y=0
            
        self.image = constants.PRINCESS_IMAGE
        
    def shouting(self): #the princess will shout "help" randomly
        number = random.randint(0,100)
        if number==3 or number==10 or number ==50:
            self.image=constants.PRINCESS_IMAGE_SHOUT
        else:
            self.image=constants.PRINCESS_IMAGE
            