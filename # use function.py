# viết hàm tìm ước
def tim_uoc(n):
    list2 = []
    for i in range(1,n+1):
        if n % i == 0:
            list2.append(i)
    return sum(list2)       
    
def perfect_number(a,b):
    print(f"Below are all perfect numbers between {a} and {b}:")
    list2 = []
    for i in range(1,n+1):
        if n % i == 0:
            list2.append(i)
    
    for i in range(a, b+1):
        if 2*i == sum(list2):
            print("{0} is a perfect number".format(i))
   
# def perfect_number(a,b):
#     for num in range(a,b+1):
#         sum = 1
#         i = 2
#         while i * i <= num:
#             if num % i == 0:
#                 sum = sum + i + num/i
#                 i += 1
#         if sum == num and num!=1:
#             print(num , "is a perfect number")
# a=int(input())
# b=int(input())
# print("Below are all perfect numbers between {} and {}:".format(a, b))
# perfect_number(a, b)  
   
a = int(input())
b = int(input())
perfect_number(a, b)


