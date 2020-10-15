# -*- coding: utf-8 -*-
"""
Created on Sat May 25 01:50:02 2019

@author: long8v
"""

import pickle

def txt_open(filename):
    with open (filename) as fp:
        txt += fp.read()
    return txt

def pickle_save(filename,object_name):
    with open(filename, 'wb') as f:
        pickle.dump(object_name, f)
        
def pickle_open(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)