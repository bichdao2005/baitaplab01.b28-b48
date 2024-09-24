# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:46:14 2024

@author: Bich Dao
BÀI 33. Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là 
số chính phương hay không? (Số chính phương là số khi lấy căn bậc 2 có 
kết quả là nguyên)
"""
import math
n= int(input("nhập vào số n:"))
while n<=0:
    n= int(input("nhập vào n:"))
cb= math.sqrt(n)    
if cb.is_integer():
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải là số chính phương")