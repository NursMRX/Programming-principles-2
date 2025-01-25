car = {
  "brand": "Ford",
  "model": "Mustang",
  "electric": False,
  "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


xItem = car.items()

print(xItem) #before the change

car["year"] = 2020

print(xItem) #after the change

car.update({"year": 2025})

print(car)


car.pop("model")
print(car)


for x, y in car.items():
  print(x, y)


car2 = car.copy()
car2.update({"brand": "McLaren Automotive"}, {"model": "McLaren"})

print(car2)




myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])




