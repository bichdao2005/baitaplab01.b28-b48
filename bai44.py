# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:32:18 2024

@author: Bich Dao
Bài 44
"""
s=0
n =int(input("nhập n: "))
while n<=0:
    n=int(input("nhập n: "))
for i in range(1, n+1) :
    s+= (2*i+1)/(2*i+2)
print(round(s,2))
    
