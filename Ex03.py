# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:42:29 2020
假設這期的統一發票中獎號碼為01272636、39412201、94586356。請設計一程式讓使用者輸入一組發票號碼即可印出中獎金額。
   (其中末三碼相同獎金200元；末四碼相同獎金1000元；末五碼相同獎金4000元；末六碼相同獎金10000元；末七碼相同獎金40000元；號碼全部相同獎金200000元。
@author: ASUS
"""
prize1=[0,1,2,7,2,6,3,6]
prize2=[3,9,4,1,2,2,0,1]
prize3=[9,4,5,8,6,3,5,6]
input_string = input("輸入你的號碼:")
number  = input_string.split()
number = [ int(i) for i in number ]
count1=0
count2=0
count3=0
for i in range(7,-1,-1):
    if prize1[i] == number[i]:

        count1+=1
    else:
        break
for i in range(7,-1,-1):
    if prize2[i] == number[i]:

        count2+=1
    else:
        break
for i in range(7,-1,-1):
    if prize3[i] == number[i]:

        count3+=1
    else:
        break
if count1>3:
    count=count1
if count2>3:
    count=count2
if count3>3:
    count=count3
if count== 8:
    print(200000)
elif count== 7:
    print(40000)
elif count== 6:
    print(10000)
elif count== 5:
    print(4000)
elif count== 4:
    print(1000)
elif count== 3:
    print(200)