# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:44:51 2024

@author: Bich Dao
BÀI 46. Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau:
2x + 7y + 9z = 979 với (x, y, z > 0)
"""
#2*x +7+9= 979 >x=490
#2+7*y+9=979 >140
#2+7+9*z=979 >
bo_nghiem =[]
for x in range (1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x +7*y +9*z ==979:
                bo_nghiem +=[(x,y,z)]
if bo_nghiem :
    print(f'{bo_nghiem}')
                
