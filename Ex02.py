# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:17:50 2020
輸入一個字串, 並把它反向輸出
@author: User
"""

input_str=input();
reverse_str = ''
for i in input_str:
    reverse_str = i + reverse_str 
print(reverse_str)
