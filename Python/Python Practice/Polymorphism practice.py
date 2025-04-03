"""class Shape:
    pie=3.14
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Circle Area:", self.pie*self.radius*self.radius)

class Rectangle(Shape):

    def __init__(self,len,width):
        self.len = len
        self.width = width

    def area(self):
        print("Rectangle Area:", self.len*self.width)

circle=Circle(5)

rectangle = Rectangle(8,25)

circle.area()

rectangle.area()

class Calc:

    def add(*args):
        if len(args)==1:
            for i in args: i=i*i
            print("Square",i)
        elif len(args)==2:
            sum=0
            for i in args: sum=sum+i
            print("Addition",sum)
        else:
            result = 1
            for num in args: result *= num
            print("Product",result)

Calc.add(5) 
Calc.add(10, 20) 
Calc.add(2, 3, 4)
"""
