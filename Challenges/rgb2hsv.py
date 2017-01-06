# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 10:28:01 2017

@author: della
"""

"""
Given some color in the rgb format, your task is to convert it into the hsv format. The result should be an array of three formatted numbers, where:

    the first number is the Hue value rounded to the nearest integer;
    the second number is the Saturation value in percent rounded to the 10th place;
    the third number is the Value value in percent rounded to the 10th place.
"""
    
def rgb2hsv(rgb):
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0
    cmax = max(r,g,b)
    cmin = min(r,g,b)
    delta = cmax - cmin
    #Calculate hue
    if delta == 0:
        h = 0
    elif cmax == r:
        h = (60 * ((g-b)/delta) + 360) % 360
    elif cmax == g:
        h = (60 * ((b-r)/delta) + 120) % 360
    elif cmax == b:
        h = (60 * ((r-g)/delta) + 240) % 360
    #Calculate saturation 
    if cmax == 0:
        s = 0.0
    else:
        s = round((delta/cmax)*100,1)
    #Calculate vibrance
    v = round(cmax*100,1)
    return list([str(round(h))[:-2], str(s), str(v)])