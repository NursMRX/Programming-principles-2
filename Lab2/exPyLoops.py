#While loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)