# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:22:34 2019

@author: USER
"""

from matplotlib import font_manager, rc
import winsound

def font_setting():
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
    return None

def make_sount():	
	duration = 1000  # milliseconds
	freq = 440  # Hz
	winsound.Beep(freq, duration)
