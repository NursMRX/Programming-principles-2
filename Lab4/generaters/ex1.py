def squares_of_number(number):
    for num in range(1, number + 1):
        if num**2 < number:
            yield num**2
        else:
            continue

number = int(input("Enter the number: "))
square = squares_of_number(number)

try:
    while True:
        print(next(square), end=" ")
except:
    pass