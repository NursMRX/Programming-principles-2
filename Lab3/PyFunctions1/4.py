from random import randint
from math import sqrt

def filter_prime(numbers):
    PrimeNumbers = []
    for num in numbers:
        if num < 2:  
            continue
        check = True
        for i in range(2, round(sqrt(num)) + 1):
            if num % i == 0: 
                check = False
                break
        if check:
            PrimeNumbers.append(num)
    return PrimeNumbers


numbers = [randint(1, 30) for n in range(30)]

print(f"Generated numbers: {numbers}")
print(f"Prime numbers: {filter_prime(numbers)}")
