'''my_list=[8.5,5.6,6.7,7.8,8.4,4.9,9.0,0.5,-1.2,-8.9]
my_list.sort()
print(my_list)
print(len(my_list))
print("Enter khoảng [a, b]: ")
a = float(input())
b = float(input())

 [-8.9, -1.2, 0.5, 4.9, 5.6, 6.7, 7.8, 8.4, 8.5, 9.0]
that is algrithm:
[min(my_list);max(my_list)] [a, b]
  if a<min(my_list) and b


synthetic all case can happen:

a <min
    if b>max:
        print("All elements in list belong to [{a},{b}]")
    else:
        ls = my_list.remove[b]
        if len(ls) == 1:
            print("Some elements in list do not belong to [{a},{b}]")
        elif len(ls)<1:
            print("All elements in list do not belong to [{a},{b}]")
    
a> min 
   if b>max
    
   else:
    
else: sai

my_list=["Ổi", 8.0, "Lê", 12.5, "Táo", 13.5, "Đào", 9.6,"Nho", 20.2]

del my_list[0:10:2]


thucte = ["Ổi", 8.0, "Lê", 12.5, "Táo", 14.5, "Đào", 9.6,"Kiwi", 18.4,"Cherry", 30.8]

del thucte[0:12:2]



print("Phần chênh lệch là: "+str(sum(thucte)-sum(my_list)))


# câu nói kinh điển giữ đầu bỏ đuôi
name = input("Hello! What is your name? ")
print("Hi " + name + ", good to see you!")
feeling = input("How are you? ")

'''     
'''

from turtle import *
from random import randint
colormode(255)
def mau():
    color(randint(0, 255), randint(0, 255), randint(0, 255))
for _ in range(6):
    i = 1
    mau()
    for _ in range(150):
        forward(1)
        pensize(i)
        i += 0.5
    pensize(1)
    goto(0, 0)
    left(360/6)    
'''
# # define a matrix A
# A = [[5, 4, 3],
#      [2, 4, 6],
#      [4, 7, 9],
#      [8, 1, 3]]
# # define an empty matrix of reverse order
# transresult = [[0, 0, 0, 0],
#                [0, 0, 0, 0],
#                [0, 0, 0, 0]]
# # use nested for loop on matrix A
# for a in range(len(A)):
#     for b in range(len(A[0])):
#         transresult[b][a] = A[a][b]

# list = [{"name": "Hung", "point": 10},
#        {"name": "Giang", "point": 10},
#        {"name": "Hieu", "point": 9}]

# list1 = map(lambda x: sorted(x), list)
# print(list1)

# class Circle:
#     pi = 3.1416
#     def __init__(self, radius):
#       self.radius = radius
    
#     def circle(self):
#       r = float(input())
    
#     def circumference(self):
#       return 2 * self.pi * self.radius
    
#     def areas(self):
#       return self.pi * self.radius**2
    
# r=float(input())
# print("PI:",Circle.pi)
# print("Radius:", r)
# a = Circle(r)

# print("Circumference: "+str(a.circumference()))
# print("Area: "+str(a.areas()))




