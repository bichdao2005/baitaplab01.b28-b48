# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:11:11 2024

@author: Bich Dao
BÀI 35. Tính S = 1 + 2 + 3 + ... + n (n nguyên và lớn hơn 0)
"""
tong=0
n=int(input("nhập vào n:"))
while n<=0:
    n= int(input("nhập vào n:"))
for i in range(1,n+1):
    tong+=i    
print(tong)
