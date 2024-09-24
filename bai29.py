# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:23:59 2024

@author: Bich Dao
bài 29 tính tổng các chữ số N nguyên dương. 
(Nhập N = 6789 thì 6+7+8+9 = 30)
"""
n= int(input("nhập vào n có 4 chữ :"))
while n<1000 or n>9999:
    n=int(input("nhập vào n:"))
a=n//1000
b=(n%1000)//100
c=(n%1000)%100//10
d=(n%1000)%100%10
print("tổng các chữ số của n là:",a+b+c+d)

