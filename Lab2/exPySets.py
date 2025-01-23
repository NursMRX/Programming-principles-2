thisset = {"apple", "banana", "cherry"}
print(thisset)


print("banana" in thisset)

for x in thisset:
    print(x)

thisset.add("orange")

print(thisset)

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset.remove("banana")

print(thisset)

for x in thisset:
    print(x)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


set5 = {"a", "b" , "c"}
set6 = {1, 2, 3}

set5.update(set6)
print(set5)

set7 = {"apple", "banana", "cherry"}
set8 = {"google", "microsoft", "apple"}

set9 = set7 - set7
print(set9)
