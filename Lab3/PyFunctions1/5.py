from itertools import permutations


def Perm(string):
    for perm in permutations(string):
        print(''.join(perm))


string = str(input("Enter a word: "))
Perm(string)