# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:00:42 2024

@author: Bich Dao
BÀI 38. Tính S = 1 * 2 * 3 * ... * n (với n lẻ > 0)
"""
s=1
n=int(input("nhập vào n:"))
while n<=0 or n%2==0:
    n=int(input("nhập vào n:"))
for i in range(1, n+1):
    s*=i
print(s)
