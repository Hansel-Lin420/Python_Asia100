# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:57:00 2020
請設計一樂透亂數選號程式，由1~42中選出6個不重覆的數字組合並輸出。
@author: ASUS
"""
import random as rnd
l = []
for i in range(42):
    number = rnd.randint(1,42)
    l.append(i+1)
print(rnd.sample(l, 6))


