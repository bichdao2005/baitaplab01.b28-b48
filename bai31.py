# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:14:57 2024

@author: Bich Dao
BÀI 31. Nhập vào ba số nguyên dương. Kiểm tra xem 3 số đó có lập thành tam giác 
không? Nếu có hãy cho biết tam giác đó thuộc loại nào? (Cân, vuông, 
đều...).
"""
a= float(input("nhập cạnh a:"))
b=float(input("nhập cạnh b:"))
c=float(input("nhập cạnh c:"))
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        loai="tam giác đều"
    elif a==b or a==c or b==c:
        loai="tam giác cân"
    elif a*a==b*b+c*c or b*b==c*c+a*a or c*c==b*b+a*a:
        loai= "tam giác vuông"
    elif a*a>b*b+c*c or b*b>c*c+a*a or c*c>b*b+a*a:
        loai="tam giác tù"
    else:
        loai="tam giác nhọn"
    print("{0},{1},{2} là ba cạnh của tam giác {3}".format(a,b,c,loai))    
else:
    print("đây không phải tam giác")       