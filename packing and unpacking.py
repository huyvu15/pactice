# làm quen unpacking and packing

# odd_number = (1, 3, 5)
# even_number = (2, 4, 6)
# numbers = (*odd_number,*even_number)
# print(numbers)

# # tính dãy fibonacci sử dụng unpackage
# def fib(n):
#     a, b = 1,1
#     for i in range(n):
#         a, b = b, a+b
#     print(a)
    
# n = int(input())

# fib(n)


# authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
# for first_name, last_name in authors:
#     print("First name:", first_name+",", "Last name:", last_name)

# def statistic(*x):
#     sum1 = 0
#     sum2 = 0
#     x = list(map(int, x))
#     for i in x:
#         sum1 = sum1 + i
#     mean = sum1/(len(x))
#     for i in x:
#         sum2 = sum2+(i-mean)**2
#     variance = sum2/len(x)
#     print("Mean:",mean)
#     print("Variance:",variance)

# string=input().split(" ")
# print(string)
# statistic(*string)

def statistic(x):
    mean = sum(x) / len(x)
    variance = sum((i - mean) ** 2 for i in x) / len(x)
    print("Mean:",mean)
    print("Variance:",variance)

data = list(map(lambda a: float(a), x))
statistic(data)
