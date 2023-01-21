# Đếm số lẻ ko chia hết cho 5 và 7
a = int(input())
b = int(input())
count = 0

# Cách khác
list1 = []
list2 = []
for k in range(a, b+1):
    if k % 5 == 0 or k % 7 == 0:
        continue
    list1.append(k)
        
for i in list1:
    if i % 2 == 0:
        continue
    list2.append(i)
print(len(list2))




# if a <=b:
#     for i in range(a, b+1):
#         if i%2==0:
#             continue
#         if i % 5==0 or i % 7 ==0:
#             continue
#         print(i)
#         count+=1
#     print(count)
# else:
#     for i in range(b, a-1, -1):
#         if i%2==0:
#             continue
#         if i % 5==0 or i % 7 ==0:
#             continue
#         count+=1
#     print(count)    
    
    

    

            