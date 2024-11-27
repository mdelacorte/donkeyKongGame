#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:57:01 2019

@author: mariadelacorte
"""
import constants

class Plat:
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
            
        self.image= constants.PLATFORM_IMAGE1
        self.image2=constants.PLATFOM_IMAGER
        self.imagePrincess = constants.PLATFORM_IMAGE2
                #information of images from image bank it should
                #be the coordinates of the image NOT THE IMAGE
                
        