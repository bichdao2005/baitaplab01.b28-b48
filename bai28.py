# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:59:09 2024

@author: Bich Dao
BÀI 28. Nhập vào số N từ bàn phím (điều kiện N nguyên dương) nếu người dùng 
nhập không đúng thì bắt nhập lại. Sao đó in ra tất cả ước số của N.
"""

n= int(input("nhập vào n: "))
while n<=0:
    n= int(input("nhập vào n:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")