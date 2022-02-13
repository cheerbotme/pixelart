#!/usr/bin/env python

import os

import time

from sys import exit, argv

try:
    
    from PIL import Image
    
except ImportError:
    
    exit('install pillow mod: sudo pip install pillow')

print(
"""
****************************************************************
 sprite for the raspberry pi pimoroni unicorn-hat-hd by bestape 
                            based on                            
animated weather icons for the unicorn-hat-hd by LovebootCaptain
****************************************************************
"""
)

import unicornhathd as unicorn

unicorn.brightness( .8 )

unicorn.rotation( 0 )

unicornWidth, unicornHeight = unicorn.get_shape()

count = 5

cycleTime = 0.05

folderPath = os.path.dirname(
    os.path.realpath( __file__ )
) + '/sprite/'

spriteList = [
    '00sprite.png'
    , '01sprite.png'
    , '02sprite.png'
    , '03sprite.png'
    , '04sprite.png'
    , '00sprite.png'
    , '05-1sprite.png'
    , '05-2sprite.png'
    , '06sprite.png'
    , '07sprite.png'
    , '08-1sprite.png'
    , '08-2sprite.png'
    , '09sprite.png'
    , '00sprite.png'
    , '10sprite.png'
    , '11-1sprite.png'
    , '11-2sprite.png'
    , '11-3sprite.png'
    , '12-1sprite.png'
    , '12-1sprite.png'
    , '13sprite.png'
    , '14-1sprite.png'
    , '14-2sprite.png'
    , '00sprite.png'
    , '15sprite.png'
    , '16sprite.png'
    , '17-1sprite.png'
    , '17-2sprite.png'
    , '18-1sprite.png'
    , '18-2sprite.png'
    , '19sprite.png'
    , '00sprite.png'
    , '20-1sprite.png'
    , '20-2sprite.png'
    , '21sprite.png'
    , '22sprite.png'
    , '23-1sprite.png'
    , '23-2sprite.png'
    , '23-3sprite.png'
    , '24-1sprite.png'
    , '24-2sprite.png'
    , '24-3sprite.png'
    , '25sprite.png'
    , '00sprite.png'
    , '26-1sprite.png'
    , '26-2sprite.png'
    , '26-3sprite.png'
    , '27-1sprite.png'
    , '27-2sprite.png'
    , '28-1sprite.png'
    , '28-2sprite.png'
    , '29sprite.png'
    , '00sprite.png'
    , '30-1sprite.png'
    , '30-2sprite.png'
    , '30-3sprite.png'
    , '32sprite.png'
    , '33sprite.png'
    , '34-1sprite.png'
    , '34-2sprite.png'
    , '00sprite.png'
    , '35sprite.png'
    , '36-1sprite.png'
    , '36-2sprite.png'
    , '36-3sprite.png'
    , '37-1sprite.png'
    , '37-2sprite.png'
    , '38sprite.png'
    , '39-1sprite.png'
    , '39-2sprite.png'
    , '00sprite.png'
    , '40sprite.png'
    , '41-1sprite.png'
    , '41-2sprite.png'
    , '42sprite.png'
    , '43sprite.png'
    , '44sprite.png'
    , '00sprite.png'
    , '45sprite.png'
    , '46sprite.png'
    , '47-1sprite.png'
    , '47-2sprite.png'
    , '48sprite.png'
    , '49sprite.png'
    , '50sprite.png'
]

def drawSprite( image ):
    
    try:
        
        imageHeight = int( image.size[ 1 ] / unicornHeight )
        
        imageWidth = int( image.size[ 0 ] / unicornWidth )
        
        for planeHeight in range( imageHeight ):
            
            for planeWidth in range( imageWidth ):
                
                valid = False
                
                for positionHeight in range( unicornHeight ):
                    
                    for positionWidth in range( unicornWidth ):
                        
                        pixel = image.getpixel( (
                            (
                                planeWidth * unicornWidth
                            ) + positionHeight
                            , (
                                planeHeight * unicornHeight
                            ) + positionWidth
                        ) )
                        
                        blue = int( pixel[ 2 ] )
                        
                        green = int( pixel[ 1 ] )
                        
                        red = int( pixel[ 0 ] )
                        
                        if blue or green or red:
                            
                            valid = True
                            
                        unicorn.set_pixel(
                            positionWidth
                            , positionHeight
                            , red
                            , green
                            , blue
                        )
                        
                if valid:
                    
                    unicorn.show()
                    
                    time.sleep( cycleTime )
                    
    except KeyboardInterrupt:
        
        global count
        
        count -= 1
        
        if count > 0:
            
            print(
                ': hit ^C '
                + str( count )
                + ' more time(s) to exit'
            )

def eachSprite():
    
    try:
        
        while count > 0:
            
            for sprite in spriteList:
                
                if count > 0:
                    
                    image = Image.open( folderPath + sprite )
                    
                    print( sprite )
                    
                    drawSprite( image )
                    
                else:
                    
                    unicorn.off()
                    
    except IndexError:
        
        print( 'index error' )
        
if __name__ == '__main__':
    
    eachSprite()
    
