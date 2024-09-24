# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:00:42 2024

@author: Bich Dao
BÀI 37. Tính S = 2 + 4 + 6 + ... + n (với n chẵn > 0)
"""

s=0
n=int(input("nhập  n:"))
while n<=0 or n%2!=0:
    n=int(input("nhập vào n: "))
for i in range(2,n+2,2):
    s+=i
print(s)
