n = int(input())
list = []

# code nay sai do lỗi space
# contain = []
# for i in range(n):
#     types = input().split(" ")
#     contain.append(types)

# for i in range(n):
#     if contain[i][0] == "insert":
#         list.insert(int(contain[i][1]), int(contain[i][-1]))
#     if contain[i][0] == "print":
#         print(list)
#     if contain[i][0] == "remove":
#        list.remove(int(contain[i][1]))
#     if contain[i][0] == "append":
#         list.append(int(contain[i][1]))
#     if contain[i][0] == "sort":
#         list.sort()
#     if contain[i][0] == "pop":
#         list.pop(-1)     
#     if contain[i][0] == "reverse":
#         list.reverse()

# code đúng
for _ in range(n):
    arr = []
    arr.extend(input().split())
    if arr[0] == "insert":
        list.insert(int(arr[1]), int(arr[2]))
    elif arr[0] == "print":
        print(list)
    elif arr[0] == "remove":
        list.remove(int(arr[1]))
    elif arr[0] == "append":
        list.append(int(arr[1]))
    elif arr[0] == "sort":
        list.sort()
    elif arr[0] == "pop":
        list.pop()
    elif arr[0] == "reverse":
        list.reverse()

    

 
  