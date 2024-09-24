# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:51:24 2024

@author: Bich Dao
bài 43
"""
s=0
n= int(input("nhập vào n:"))
while n<=0:
    n=int(input("nhập vào n: "))
for i in range (1,n+1):
    s+= i/(i+1)
print(round(s,2))