#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:20:48 2019

@author: mariadelacorte
"""
import constants 

class Ladder:
    
    def __init__(self,x,y):
        if x>=0:
            self.x=x
        else:
            self.x=0
        if y>=0:
            self.y=y
        else:
            self.y=0
            
        self.image = constants.LADDER_IMAGE
        self.imageP = constants.LADDER_IMAGE_PRINCESS
        self.imageUp = constants.LADDER_IMAGE_UP