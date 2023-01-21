#Tìm giá trị lớn thứ  hai trong chuỗi
n = int(input("Enter n point: "))
point_table = []

for i in range(0, n, 1):
    point_table.append(int((input())))    

# i think algrithm is we will find element max after delete that element out list (call is list1)
# continue find element max in list1. That result need find
print(point_table)
   
max = point_table[0] 
    

for i in range(1, len(point_table), 1):
    if max < point_table[i]:
        max = point_table[i]
# Delete the same elements

point_table = dict.fromkeys(point_table)
print(point_table)

unique_point_table = list(point_table)
print(unique_point_table)         

try:
    while True:
        unique_point_table.remove(max)
except ValueError:
    pass
 
print(point_table)
result = []
for i in unique_point_table:
    result.append(i)
  
print(result) 
to = result[0]     
for k in range(0, len(result), 1):
    if to < result[k]:
        to = result[k]
print(to)

        