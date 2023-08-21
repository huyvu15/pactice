# rut thăm trúng thưởng
'''Bài tập:
Xây dựng chương trình rút thăm trúng thưởng với các chức năng:
1. Thêm 1 mã số dự thưởng/sdt vào thùng
2. Xóa 1 mã số dự thưởng/sđt ra khỏi thùng
3. Quay số ngẫu nhiên lấy ra một mã số trúng thưởng/sdt 
'''

import random

# Khai báo set
thungPhieu = set() # if để là {} then python will by dictionary

# check xem nó đã nằm trong sđt chưa
#if x in thungPhieu:
    
# create a menu
while(True):
    print("------Menu--------")
    print("select function: ")
    print("1.Thêm 1 mã số dự thưởng/sdt vào thùng ")
    print("2.Xóa 1 mẫ số dự thưởng/sđt từ thùng ")
    print("3.Quay số ngẫu nhiên lấy ra mã số/sđt ")
    print("4.end")
    print("thùng phiếu hiện tại: ")
    print(thungPhieu)
    
    select = int(input())
    if (select == 1):
        sdt = input("enter phone number dự thưởng: ")
        thungPhieu.add(sdt)
    elif (select == 2):
        sdt = input("enter phone number dự thưởng need remove: ")
        thungPhieu.discard(sdt)
    elif (select == 3):
        index = random.randint(0, len(thungPhieu)-1) 
        print("Vị trí trúng thưởng"+str(index))
        i = 0
        for x in thungPhieu:
            if i == index:
                break
            i = i+1
            
        print("Chúc mừng sđt "+x+" đã trúng thưởng!")
        thungPhieu.discard(x)
        
    else:
        break
        
    x = input("Nhập phím bất kỳ để tiếp tục ")





