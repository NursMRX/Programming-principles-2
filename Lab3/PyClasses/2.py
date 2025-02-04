class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length * self.length

square_obj = Square(float(input("Enter the length of the square: ")))
print(f"Area of Square: {square_obj.area()}")