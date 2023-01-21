# Nạp chồng toán tử 
class vi_du:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "({0},{1}".format(self.a, self.b)

    def __eq__(self, other):
        c = abs(self.a)+ abs(self.b)
        d = abs(self.a)+ abs(self.b)
        return c == d
    
t1 = vi_du(1, 1)
t2 = vi_du(2, 2)

t3 = vi_du(3, 3)

print(t1==t2)
print(t3==t2)
print(t1==t3)
