# đồng hồ cát
size = int(input())

# không biết code này sai gì mà trên web nó không nhận

# i = 1
# while i <= size:
#     j = 0
#     while j < i:
#         # display space
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= size:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1

# chắc vấn đề ở chỗ này i ko được gắn kiểu này do phần thân  mình code đầu tiên nên đặt giá trị của i 
# if delete element i  = 1 then result is being wrong

# i = 1
# while i< size+1:
#     j = i
#     while j < size +1:
#         print(" ", end = "")
#         j+=1
#     k =1 
#     while k < i+1:
#         print("* ", end = "")
#         k +=1
#     print()
#     i+=1
    
i = 0
while i <= size - 1:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= size - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = size - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= size - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1