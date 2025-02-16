def even_numbers(num):
    for num in range(1, num + 1):
        if num % 2 == 0:
            yield num
        else:
            continue

number = int(input("Enter the endpoint number: "))
it = even_numbers(number)

try:
    next_even = next(it)
    while True:
        print(next_even, end='')
        next_even = next(it)
        print(', ' if next_even is not None else '', end='')

except StopIteration:
    pass