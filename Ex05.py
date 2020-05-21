# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:12:33 2020
設計一個程式由1~10的亂數隨機產生一10*10的二維陣列，將行列互換輸出(即輸出轉置矩陣)
@author: ASUS
"""
import numpy as np
import random as rnd
ary = np.zeros((10,10),dtype=int)
ary2 = np.zeros((10,10),dtype=int)

for i in range(10):
    for j in range(10):
        number= rnd.randint(1,10);
        ary[i][j]=number
        
print('未轉置前:')
print(ary)
for i in range(10):
    for j in range(10):
        ary2[i][j]=ary[j][i]
print('轉置後:')
print(ary2)