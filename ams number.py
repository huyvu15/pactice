#  Armstrong





# num = int(input())
# while num != sum:
#     count = 0
#     a = num
#     while a!=0:
#         a//=10
#         count+=1
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** (count)
#         temp //= 10
#     else:
#         if num == sum:
#             print(num,"is an Armstrong number")
#         else:
#             num =  int(input())


# code again armstrong

n = int(input())

while n !=sum:
    # kiểm tra xem n có bao nhiêu chữ số
    count=0
    a = n
    while a!=0:
        a = a//10
        count +=1
    sum = 0
    temp = n
    while temp>0:
        digit = temp %10
        sum += digit ** count
        temp //=10
    else:
        if n == sum:
            print(n, "is an Armstrong number")
        else:
            n = int(input())
        
    


