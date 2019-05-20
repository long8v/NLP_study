# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:45:54 2019

@author: USER
"""

from konlpy.corpus import kolaw,kobill
from nltk.corpus import gutenberg

def get_gutenberg():
    return gutenberg.open(gutenberg.fileids()[0]).read()

def get_klaw():
    return kolaw.open(kolaw.fileids()[0]).read()