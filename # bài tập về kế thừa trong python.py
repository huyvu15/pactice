class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
    
  def perimeter(self):
    return 2 * (self.length + self.width)
  
  def area(self):
    return self.length * self.width
  
  def display(self):
    print("The length of rectangle is: "+str(self.length))
    print("The width of rectangle is: "+str(self.width))
    print("The perimeter of rectangle is: "+str(self.perimeter()))
    print("The area of rectangle is: "+str(self.area()))
    

class Parallelepipede(Rectangle):
  def __init__(self,height):
        Rectangle.__init__(self,length,width)
        self.height = height
  
  def volume(self):
        return self.length*self.width*self.height
  
        
length = float(input())
width = float(input())

myRectangle = Rectangle(length, width)
print(myRectangle.perimeter())
print(myRectangle.area())
myRectangle.display()

height = float((input()))
myParallelepipede = Parallelepipede(length)

print("The volume of myParallelepipede is: "+str(myParallelepipede.volume()))



