# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:03:20 2020
輸入一個字元, 判斷是大寫或小寫或是其他字元
@author: ASUS
"""
ch = (input('輸入一個字元:'))
asc=ord(ch)
if asc >= 65  and asc <= 90:
    print('大寫')
elif asc >=97 and asc <=122:
    print('小寫')
else:
    print('請輸入英文字母')