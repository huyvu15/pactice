# xây dựng từ điển
'''
xây dựng 1 từ điển có các chức năng như sau (người dùng lựa chọn
chức năng thông qua menu):
1. Thêm 1 từ vựng mới (kèm nghĩa) vào từ điển.
2. Tra cứu ý nghĩa của 1 từ vựng.
3. Cập nhập ý nghĩa cho 1 từ vựng.
4. Cho phép người dùng xóa đi 1 từ vựng trong từ điển
5. Cho phép người dùng xóa toàn bộ từ vựng
6. Cho phép người dùng in ra toàn bộ từ vựng
7. Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: "Từ vựng", "Ý nghĩa"
8. kết thúc chương trình
'''
tudien = {}

while True:
    print("------Menu-------")
    print("1. Thêm 1 từ vựng mới (kèm nghĩa) vào từ điển.")
    print("2. Tra cứu ý nghĩa của 1 từ vựng.")
    print("3. Cập nhập ý nghĩa cho 1 từ vựng.")
    print("4. Cho phép người dùng xóa đi 1 từ vựng trong từ điển")
    print("5. Cho phép người dùng xóa toàn bộ từ vựng")
    print("6. Cho phép người dùng in ra toàn bộ từ vựng")
    print("7. Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: Từ vựng-Ý nghĩa")
    print("8. End program")
    
    select = int(input("enter your select: "))
    
    if select == 1 or select == 3:
        vocabulary = input("enter vocabulary: ")
        mean = input("enter mean: ")
        tudien[vocabulary] = mean
        print("added or update data!")
    elif select == 2:
        vocabulary = input("enter vocabulary: ")
        print("Ý nghĩa: ", tudien[vocabulary])
    # elif select == 3:
    #     vocabulary = input("enter vocabulary: ")
    #     mean = input("enter mean: ")
    #     tudien.update()
    elif select == 4:
        vocabulary = input("enter vocabulary need delete: ")
        tudien.pop(vocabulary)
        print("deleted")
    elif select == 5:
        tudien.clear()
        print("Deleted all data ")
    elif select == 6:
        print("list vocabulary in dictionary")
        for x in tudien.keys():
            print(x)
    elif select == 7:
        for x,y in tudien.items():
            print(x+" : "+y)
    elif select == 8:
        print("end")
        break
    else:
        print("your select not true")
    