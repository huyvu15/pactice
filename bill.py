name1 = 'orange'
price1 = 150
unit1 = 2

name2 = 'grape' #nho
price2 = 130
unit2 = 23 # đơn vị

tprice = price1+price2 #total the amount of merchandise
discount=15 # giảm giá
fprice=tprice-discount

print("S.no{:<8}Product{:<8}Unit Price".format("",""))
# print("{0}{:<8}{2}{:<8}{:<8} {5}  {6}".format(0,name1, "","",unit1, price1))

print("{:<12}".format(0),end='')
print("{:<15}{:<5}{:<2}".format(name1, unit1, price1))
print("{:<12}".format(1),end='')
print("{:<15}{:<5}{:<2}".format(name2, unit2, price2))

print("Discont:{:<24}{}".format("", 15))
print("Total:{:<26}{}".format("", fprice))






