#Tìm số nguyên dương nhỏ nhất


# sum=int(input())

# tong = 0
# i=1
# while True:
#   tong =  tong +i
#   if tong >  sum:
#     print(i)
#     break
#   i+=1




# Đồng hồ cát vạn năng
size  = int(input())
i = 0

while i<= size:
    j = 0
    while j<i:
        print("", end = " ")
        j+=1
    k =i
    while k < size:
        print("*", end =  " ")
        k+=1
    print()
    i+=1
# while i<=size:
#     j  = size
#     while i>j:
#         print("", end = " ")
#     j-=1
#     k = i
#     while k  >=j:
#         print("*", end = " ")
#     k += 1
#     print()
#     i+=1

# i = 1
# while i <= size:
#     print(" " * (i - 1) + "* " * (size - i + 1))
#     i += 1

# i = size-1
# while i >= 1:
#     print(" " * (i - 1) + "* " * (size - i + 1))
#     i -= 1