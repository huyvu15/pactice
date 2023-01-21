#bài toán xác định loại tam giác    
a=float(input())
b=float(input())
c=float(input())
tam_giac=[a>0, b>0, c>0, a+b>c, a+c>b,b+c>a]
tam_giac_vuong=[a*a+b*b==c*c, a*a+c*c==b*b, b*b+c*c==a*a]
tam_giac_can_deu=[a==b, b==c, c==a]
tam_giac_tu=[a*a+b*b<c*c, a*a+c*c<b*b, b*b+c*c<a*a]

if (all(tam_giac)):
  if (any(tam_giac_vuong)):
    print("Right triangle !")
  elif(all(tam_giac_can_deu)):
    print("Equilateral triangle !")
  elif (any(tam_giac_can_deu)):
    print("Isosceles triangle !")
  elif (all(tam_giac_tu)):
    print("Obtuse triangle !")
  else:
    print("Acute triangle !")
else:
  print("Not a Triangle !")