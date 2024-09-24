# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:35:59 2024

@author: Bich Dao
BÀI 34. Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là
số nguyên tố hay không?
"""
n= int(input("nhập vào n: "))
while n<=0:
    n = int(input("nhập n: "))
if n<2:
    print("n không phải là số nguyên tố")
else:
    for i in range (2,n+1):
        if n%i ==0:
            print("n không phải là số nguyên tố")
            break
        else :
            print("n là số nguyên tố")
            break