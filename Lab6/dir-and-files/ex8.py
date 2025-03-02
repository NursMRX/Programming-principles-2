import os 

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.X_OK):
            try:
                os.remove(path)
                print("Файл успешно удален.")
            except OSError as file:
                print(f"Ошибка удаления файла: {file}")
        else:
            print("Cannot access the file")
    else:
        print("The path does not exist")

path = input("Enter the path to the file to delete: ")
delete_file(path)