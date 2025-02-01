from math import pi

def Vol(Radius):
    V = (4/3) * pi * pow(Radius, 3)
    return V

Radius = int(input("Enter the sphere radius: "))
print(f"Volume of the sphere: {Vol(Radius):.2f}")
