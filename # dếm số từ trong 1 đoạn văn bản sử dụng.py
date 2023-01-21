# from libraries import *
# sử dụng thư viện này có thể sử dụng file khác
# nếu thiếu improt *(chọn tất cả) thì mỗi lần dùng file đó đều phải 
# libraries.<funtion>()


# dếm số từ trong 1 đoạn văn bản sử dụng for
# thuật toán hay vãi luyện
string_raw=input()
s = string_raw.strip()
print(s)

count=0


for i in range(len(s)-1):
    if s[i]==" " and s[i+1] !=" " or s[i]!=" " and s[i+1]==" ":
        count +=1
print(int((count-2)/2+2))
