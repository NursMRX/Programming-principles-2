thislist = ["apple", "banana", "cherry", "Pineapple", "Strawberry", "Kiwi", "Melon", "Mango"]
print(thislist)
print(len(thislist))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

i = 0
while i < len(thislist):
    print(thislist[i]) 
    i = i + 1

newlist = [x for x in thislist if "a" in x]
print(newlist)

thislist.sort()
print(thislist)

mylist = thislist.copy()
print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
