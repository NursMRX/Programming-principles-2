def copy_file(file1, file2):
    try:
        with open(file1, 'r') as source:
            with open(file2, 'w') as dest:
                dest.write(source.read())
        print("File contents copied successfully")

    except FileNotFoundError:
        print("Source file not found")
    except IOError:
        print("Error copying file contents")

source_file = input("Enter path to source file: ")
destination_file = input("Enter path to destination file: ")
copy_file(source_file, destination_file)