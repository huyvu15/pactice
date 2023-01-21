#Xấp xỉ Taylor
x=float(input())

sum =  0
i = 1

while abs((((-1)**(i+1))/i)*(x**i)) >= 1e-5:
    sum = sum + ((((-1)**(i+1)))/i)*(x**i)
    i+=1
else:
  print(f"Value of: ln(x+1) với x = {x} is: {sum}")


