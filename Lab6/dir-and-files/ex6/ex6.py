def generate_files():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for let in alphabet:
        file_name = let + '.txt'
        with open(file_name, 'w') as file:
            file.write("This is the file" + let)


if __name__ == "__main__":
    generate_files()