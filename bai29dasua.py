# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:19:09 2024

@author: Bich Dao
"""

#Bài 29 Tính tổng các chữ số N nguyên dương. (Nhập N = 6789 thì 6+7+8+9 = 30)
n = int(input("Nhập N: "))
s = 0
while n <= 0:
    n = int(input("Nhập N: "))
for i in range(1, n + 1):
    s += n % 10
    n //= 10
print("Tổng các chữ số N là:", s)

