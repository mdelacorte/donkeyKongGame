#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:32:50 2019

@author: mariadelacorte
"""

import constants

class DonkeyKong:
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
            
        self.image= constants.DONKEY_IMAGE_F
                #information of images from image bank it should
                #be the coordinates of the image NOT THE IMAGE
                
        