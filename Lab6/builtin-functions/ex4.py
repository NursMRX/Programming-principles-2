def square_root_after_milliseconds(number, milliseconds):
    start_time = milliseconds 
    current_time = 0
    while current_time < start_time:
        current_time += 0.00005
    square_root = number ** 0.5
    return square_root

def main():
    number = int(input("Введите число: "))
    milliseconds = int(input("Введите количество миллисекунд: "))
    result = square_root_after_milliseconds(number, milliseconds)
    print(f"Квадратный корень из {number} после {milliseconds} миллисекунд составляет {result}")

main()