thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)

print(thistuple[-1])
print(thistuple[2:5])

y = list(thistuple)
y[1] = "cherry"
x = tuple(y)
print(x)

y1 = list(thistuple)
y1.remove("apple")
thistuple = tuple(y1)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


for i in range(len(thistuple)):
    print(thistuple[i])


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)