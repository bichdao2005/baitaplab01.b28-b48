# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:06:14 2024

@author: Bich Dao
bài 40
"""
s=0
n=int(input("nhập vào n:"))
while n<=0:
    n = int(input("nhập vào n:"))
for i in range(1, n+1):
    s+=1/(2*i)
print(round(s,2))
