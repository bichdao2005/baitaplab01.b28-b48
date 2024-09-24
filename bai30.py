# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:14:57 2024

@author: Bich Dao
BÀI 30. Viết chương trình nhập vào tháng năm. Hãy cho biết tháng đó có bao nhiêu 
ngày? (Để kiểm tra năm nhuận Dương lịch, bạn lấy năm đó chia cho 4. Nếu 
chia hết cho 4 thì năm đó là năm nhuận. Với các năm tròn thế kỷ, có 2 số
00 ở cuối thì lấy số năm chia cho 400. Nếu chia hết cho 400 thì là năm 
nhuận ~ Năm nhuận là năm chia hết cho 4 và không chia hết cho 100 hoặc 
chia hết cho 400)
"""
month=int(input("nhập vào tháng: "))
year=int(input("nhập vào năm: "))
if 1<=month<=12:
    if month in [1,3,5,7,8,10,12]:
        ngay=31
    elif month==2:
        if year%400==0 or ((year%4==0) and (year%100!=0)):
            ngay=29
            print("năm nhuận")
        else: 
             ngay=28
             print("năm không nhuận")
    else:
        ngay=30  
    print(f"tháng {month} có {ngay} ngày")