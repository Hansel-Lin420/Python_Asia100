# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:44:56 2020
輸入一個字元, 轉換其大小寫輸出 (大寫 ->小寫, 小寫->大寫)
@author: ASUS
"""

ch = (input('輸入一個字元:'))
asc=ord(ch)
if asc >= 65  and asc <= 90:
    print(ch.lower())
elif asc >=97 and asc <=122:
    print(ch.upper())
else:
    print('請輸入英文字母')