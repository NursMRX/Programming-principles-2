from itertools import pairwise

def has_33(nums):
    pairs = list(pairwise(nums))
    return (3, 3) in pairs

size = int(input("Enter the list size: "))
numbers = []
for num in range(size):
    num = int(input("Enter an element of the list: "))
    numbers.append(num)

print(has_33(numbers))
