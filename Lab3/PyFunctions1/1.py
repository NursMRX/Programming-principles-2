def ConvertGramToOunces(Gram):
    ounces = Gram / 28.35
    return ounces

gram = int(input("Enter the gram: "))

print(ConvertGramToOunces(gram))