# xác định từ dài nhất trong văn bản
string=input()
a = string.split()
print(a)

# for i in a:
#     c.append(len(i))
# print(c)
b = len(a[0])
for i in range(1,len(a), 1):
    if len(a[i])>b:
        b = len(a[i]) 
        c = a[i]           
        
print(c)   
print("The longest string is \"{0}\" with ".format(c), end ='')
print(str(b)+" charecters")    