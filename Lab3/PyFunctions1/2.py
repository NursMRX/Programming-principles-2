def ConvertToCelsius(F):
    TempInCelsius = (5 / 9) * (F - 32)
    return TempInCelsius


temperature = int(input("Enter the temperature in Fahrenheit: "))
print(f"{temperature} degree in fahrenheit will be {ConvertToCelsius(temperature):.2f}")