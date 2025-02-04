import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y
    def show_coordinates(self):
        print(f"({self.x}; {self.y})")
    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move
        print(f"New coordinates after moving: ({self.x}; {self.y})")
    def dist(self):
        distance = math.sqrt((self.x - self.initial_x)**2 + (self.y - self.initial_y)**2)
        return distance

initial_point = Point(float(input("x coordinate: ")), float(input("y coordinate: ")))
initial_point.show_coordinates()
x_move = float(input("new x coordinate: "))
y_move = float(input("new y coordinate: "))
initial_point.move(x_move, y_move)
distance_after_move = initial_point.dist()
print(f"Distance between initial point and new point after moving: {distance_after_move}")