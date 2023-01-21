#test kĩ thuật comperhension

# print the numbers have '3' in it
# n=int(input())
# three = [z for z in range(1,n+1,1) if n >99 and n <1000 ]
# print(three)

# # print space " " have in string
# spaces = [z for z in string if ' ' in str(z)]

# remove phonetic "ueoai" out string
# sentence=input()
# result = [a for a in sentence if a not in "ueoai"]
# print("".join(result))

string=input()
string = string.split(" ")
print(string)
result = [a for a in string if len(a)<5]

print("".join(result))


