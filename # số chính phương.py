# số chính phương
def square_number(n):
    list1 = []
    for i in range(0, n+1, 1):
        for j in range(0, int(i**0.5)+1,1):
            if i == j**2:
                list1.append(i)
    return print(list1)
        
        
        
num = int(input())
square_number(num)