# -*- coding: utf-8 -*-
"""
將一連串數字(每個數字為0~9)輸入, 計算其和. Ex: 輸入 12345, 輸出為 15 (1+2+3+4+5=15)

Created on Sat May 16 18:48:17 2020

@author: User
"""
input_number = input()
sum = 0
for i in (input_number):
  sum += int(i)
print(sum)
