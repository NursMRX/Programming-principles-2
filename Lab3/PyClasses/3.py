class Shape:
    def __init__ (self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length = float(input("length: "))
        self.width = float(input("width: "))
    def area(self):
        return self.length * self.width
rectangle_obj = Rectangle()
print(f"Area of Rectangle: {rectangle_obj.area()}")