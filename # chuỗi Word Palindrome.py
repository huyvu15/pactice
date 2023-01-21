# chuỗi Word Palindrome
string = input()
d = string.strip()
a = d.split(" ")
len = len(a)
print("Text has "+str(len)+" words.")
b = int(len/2)

if a[0:b]==a[:-b-1:-1]:
  print("Word Palindrome")
else:
  print("NOT Word Palindrome")