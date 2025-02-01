from PyFunctions1 import RevString
from PyFunctions1 import Vol


sentence = str(input("Enter the sentence: "))
RevString(sentence)

Radius = int(input("Enter the sphere radius: "))
print(f"{Vol(Radius):.2f}")


