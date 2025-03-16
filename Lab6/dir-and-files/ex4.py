import os
def count_lines(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                num_lines = len(lines)
                print(f"Количесвто строк в файле: {num_lines}")
        except FileNotFoundError:
            print("Файл не найден")
    else:
        print("Файл не существует")
        
if __name__ == "__main__":
    filename = input("Введите назаниие файла: ")
    count_lines(filename)