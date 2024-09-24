# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:32:42 2024

@author: Bich Dao
BÀI 32. Viết chương trình tính tiền cước TAXI. Biết rằng: 1 km đầu tiên là 15000đ, 
từ km thứ 2 đến thứ 5 giá là 13500đ, từ km thứ 6 giá là 11000đ, nếu đi 
hơn 120km thì sẽ được giảm 10% trên tổng tiền
"""
s= float(input("nhập vào quãng đường đi được: "))
if s==1:
    tien=15
elif 1<s<=5:
    tien= 15+ (s-1)*13.5
elif s>=6:
    tien= 15+ 4*13.5 +(s-5)*11
elif s>120:
    tien=(15+ 4*13.5 +(s-5)*11)*0.9
print("số tiền phải trả là:", tien)
