def RevString(string):
    words = string.split()
    words = words[::-1]
    print(' '.join(words))


sentence = str(input("Enter the sentence: "))
RevString(sentence)