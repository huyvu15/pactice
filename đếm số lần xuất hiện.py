# Đến số lần xuất hiện của 1 số i trong mảng
numbers=[1,3,2,4,5,2,3,6,7,5,8,1,2,2,4,9,3,4,3,4,5,1,2,3,2,2,2,3,4]
i= int(input())
count = numbers.count(i)
convert_number = {0:"zero",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"night", 10:"ten"}

print("Numbers "+str(i)+" appear "+convert_number[count]+" time in the list!")
