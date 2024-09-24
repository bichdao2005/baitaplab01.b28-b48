# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:00:27 2024

@author: Bich Dao
bài 42
"""
s=0
n=int(input("nhập vào n:"))
while n<=0:
    n= int(input("nhập vào n:"))
for i in range(1, n+1):
    s+=1/(i*(i+1))
print(round(s,2))