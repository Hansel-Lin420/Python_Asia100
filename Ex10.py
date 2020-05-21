# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:22:03 2020
迴文(palindrome)是指從前面讀和從後面讀都相同的一段文字. 請撰寫一個程式讀入一個字串,判斷它是否為迴文。
例如下列字串都是迴文:12321,AABBCCBBAA
@author: ASUS
"""
string=input()
length = len(string)
flag = True
for i in range(length):
    if string[i]==string[length-i-1]:
        flag=True
    else:
        flag=False
if flag == True:
    print('是迴文')
else:
    print('不是回文')
        