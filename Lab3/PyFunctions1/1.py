def ConvertGramToOunces(Gram):
    ounces = Gram / 28.35
    return ounces

gram = int(input("Enter the gram: "))

print(f"{gram} gram in ouncec will be {ConvertGramToOunces(gram)}")