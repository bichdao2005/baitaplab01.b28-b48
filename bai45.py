# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:35:59 2024

@author: Bich Dao
bài 45
"""
s=0
tu=1
mau=0
n =int(input("nhập vào n: "))
while n<=0:
    n=int(input("nhập n: "))
x= float(input("nhập vào x: "))
for i in range(1,n+1): 
    tu=x**i
    mau= mau+i
    s += tu/mau
print(round(s,2))
