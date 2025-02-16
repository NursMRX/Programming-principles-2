def check_divisible_3_and_4(endpoint):
    for num in range(1, endpoint):
        if num % 3 == 0 and num % 4 == 0:
            yield num
        else:
            continue


endpoint_num = int(input("Enter the number: "))
it = check_divisible_3_and_4(endpoint_num)

try:
    while True:
        print(next(it), end=' ')
except StopIteration:
    pass