import os 

def path_exist_check(path):
    if os.path.exists(path):
        print("\nPath is exist\n")
        filename = os.path.basename(path)         
        directory = os.path.dirname(path)  
        print("Имя файла:", filename)
        print("Путь к каталогу:", directory)
    else:
        print("Path does not exist")

path = input("Enter path: ")
path_exist_check(path)