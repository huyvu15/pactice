# Chuỗi Palindrome
s = input()

if s[::1] == s[::-1]:
    print("Chuỗi vừa nhập là một chuỗi Palindrome!")
else:
    print("Chuỗi vừa nhập KHÔNG phải là một chuỗi Palindrome!")