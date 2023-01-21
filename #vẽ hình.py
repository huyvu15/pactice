#vẽ hình 
# code kim cương may mắn
# size=int(input())
# for i in range(size+1):
#   for j in range(size-i+4):
#     print(end = ' ')
#   for j in range(i+1):
#     print("*", end = ' ')
#   print()
  
# for i in range(size):
#   for j in range(i+1+4):
#     print(end = ' ')
#   for j in range(size-i+1, 1, -1):
#     print("*", end = ' ')
#   print()     
    
    
size = int(input())
k = 2 * size - 2 #k = 8
for i in range(0, size):
    for j in range(0, k):
        print(end=" ")
    k = k - 1 # 
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = size - 2

for i in range(size, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")       