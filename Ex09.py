# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:13:15 2020
讓使用者輸入性別與身高，並依據男女不同, 幫她(他)計算並輸出其標準體重 (男：(身高-170)*0.6+62 女：(身高-158)*0.5+52)。
@author: ASUS
"""
gender=input('請輸入性別:')
height=(int)(input('請輸入身高:'))
bmi=0
if gender == '男':
    bmi=(height-170)*0.6+62
elif gender == '女':
    bmi=(height-158)*0.5+52
print(bmi)