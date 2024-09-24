# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:09:49 2024

@author: Bich Dao
"""

s=0
n=int(input("nhập vào n:"))
while n<=0:
    n = int(input("nhập vào n:"))
for i in range(1, n+1):
    s+=1/i
print(round(s,2))