import math
number_sides = int(input("Input number of sides: "))
lenght_side = int(input("Input the length of a side: "))
area_of_polygon =(number_sides * pow(lenght_side, 2)) / (4 * math.tan(math.pi / number_sides))
print(f"The area of the polygon is: {area_of_polygon}")