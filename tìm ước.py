n=int(input())
count = 0
divisors = []

if n>0:
  for z in range(1, n+1, 1):
    if n%z==0:
      count +=1
      divisors.append(z)
print("{0} have {1} divisors".format(n, count))
print("They are: ", end = '')
for i in  divisors:
    print(i, end = ' ')
print("!")   