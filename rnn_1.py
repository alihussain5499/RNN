# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:43:41 2019

@author: ali hussain
"""

line=" I love to eat brain."
line=line.lower()
print(line)

from nltk.tokenize import word_tokenize

words=word_tokenize(line)
print(words)

len(set(words))

i=0
ind={}
for w in set(words):
    ind[w]=i
    i+=1
    
print(ind)    

x=[]
import numpy as np
for w in words:
    z=np.zeros(len(set(words)))
    z[ind[w]]=1
    x.append(z)
print(x) 

x=np.array(x)
print(x)   

X=x[0:-1,:]
print(X)

Y=x[1:,:]
print(Y)

idx=ind
ridx=dict(list(zip(idx.values(),idx.keys())))
print(ridx)

decodeX=[ridx[int(np.where(arr==1)[0])] for arr in X]
print(decodeX)


decodeY=[ridx[int(np.where(arr==1)[0])] for arr in Y]
print(decodeY)






















