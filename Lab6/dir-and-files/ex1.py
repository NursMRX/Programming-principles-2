import os

def check_dir_or_file(path):
    directories = []
    files = []
    items = os.listdir(path)

    for item in items: 
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        else:
            files.append(item)

    return directories, files


path = input("Enter path: ")
directories, files = check_dir_or_file(path)

print("Directories: ")
for directory in directories:
    print(directory)

print("\nFiles: ")
for file in files:
    print(file)