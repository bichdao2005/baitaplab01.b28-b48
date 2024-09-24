# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:23:27 2024

@author: Bich Dao
BÀI 36. Tính S = 1**2 + 2**2 + 3**2 + ... + n**2
(n nguyên và lớn hơn 0)
"""
s=0
n= int(input("nhập vào n: "))
while n<=0:
    n= int(input("nhập vào n:"))
for i in range(1,n+1):
    s+= i**2
print(s)

