# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:51:29 2019

@author: USER
"""


def eojeol(text,n=2):
    ngram=list()
    tokens=text.split()
    for i in range(len(tokens)-(n-1)):
        ngram.append(" ".join(tokens[i:i+n]))
    return ngram

def umjeol(text,n=2):
    ngram=list()
    for i in range(len(text)-(n-1)):
        ngram.append("".join(text[i:i+n]))
    return ngram


def ngram(data,n=2):
    result=defaultdict(int)
    for term,freq in data.items():
        tokens=term.split()
        for i in range(len(tokens)-(n-1)):
            result[" ".join(tokens[i:i+n])]+=freq
    return result

def mergeNgram(data,n=2):
    newData={}
    maxKey=max(ngram(data,n),key=ngram(data,n).get)
    for term, freq in data.items():
        newKey=term.replace(maxKey,"".join(maxKey.split(" ")))
        newData[newKey]=freq
    return newData