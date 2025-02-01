from itertools import permutations

string = str(input("Enter a word: "))
for perm in permutations(string):
    print(''.join(perm))