
count = 0

str1 = str(input())
str2 = str(input())

str1 = str1.upper()    
str2 = str2.upper()    

str1 = str1.rstrip() # delete the last element of string 
str2 = str2.rstrip()
        
x = 0

# if element from i;i+len(str2)

for i in range(0, len(str1), 1):
    if str1[i:i+len(str2)] == str2:
        count = count+1
 
print(count)

# note to when I have free time, I do
# duyệt phần tử lần lượt so sanh chuỗi con với lần lượt các chuỗi có len = len(str(con))       
#print(count)  

# test code nice game in the my facebook 
'''
my_string = 'python'
x = 0

for i in my_string:
    x = x+1
    print(my_string[0:x])

for i in my_string:
    x = x -1
    print(my_string[0:x])    
              
'''
