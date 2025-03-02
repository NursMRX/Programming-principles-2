def multiply(list1):
    result = 1
    for i in list1:
        result *= i
    return result
numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = multiply(numbers)
print(result)