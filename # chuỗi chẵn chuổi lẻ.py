# chuỗi chẵn chuổi lẻ+chuỗi đối xứng


# chuỗi chẵn lẻ
# s = input()
# print(s)
# s1 = s[1::2]
# s2 = s[::2]
# print(s1)
# print(s2)
# if s2 > s1:
#     print("Even Bias!")
# elif s1 > s2:
#     print("Odd Bias!")
# else:
#     print("Balance String!") 
# tìm chuỗi đối xứng
string = input()
n = int(len(string)/2)
print(len(string))
print(n)
if len(string)>2*n:
    print("The central point of the string is "+string[n]+".")
    print(string[0:n+1:1])
    print(len(string[0:n+1:1]))
    print(string[-1:-n-1:-1])
    print(len(string[-1:-n-1:-1]))  
    if string[0:n+1:1]==string[-1:-n-1:-1]:
        print("Symmertical String!")
    elif len(string[0:n+1:1])>len(string[-1:-n-1:-1]):
        print("Left Bias!")
    else:
        print("Right Bias!")          
else:
    print("There is no central point.") 
    print(string[0:n:1])
    print(len(string[0:n:1]))
    print(string[-1:-n-1:-1])
    print(len(string[-1:-n-1:-1]))
    if string[0:n:1]==string[-1:-n-1:-1]:
        print("Symmertical String!")
    elif len(string[0:n:1])>len(string[-1:-n-1:-1]):
        print("Left Bias!")
    else:
        print("Right Bias!")                


 

# if string[0:n:1]==string[-1:-n-1:-1]:
#         print("Symmertical string!")
# elif len(string[0:n:1])>len(string[-1:-n-1:-1]):
#         print("Left Bias!")
# else:
#         print("Right Bias!")          

