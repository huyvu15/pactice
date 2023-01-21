# tập mục phổ biến
items={1,2,3,4,5,8,9,12,15,17,21,25,27,31,32,38,40,44,48,50}
n=int(input())
count = 0
for i in range(n):
    a = input().split(" ")
    b = set(map(int, a))
    if len(b & items) >= 0.4*len(items):
        count+=1
else:
    if count >= 0.4*n:
        print("YES")
    else:
        print("NO")    

    