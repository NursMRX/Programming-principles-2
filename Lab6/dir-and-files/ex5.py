import os 

def write_list_to_file(filename, cars):
    try:
        with open(filename , 'a') as file:
            for car in cars:
                file.write(car + '\n')
        print("The list has been successfully added to the file")

    except IOError:
        print("Error writing to file")


filename = input("Enter file name: ")
cars = []

while True:
    car_name = input("Enter car name or 's' to finish: ")
    if car_name.lower() == 's':
        break
    else:
        cars.append(car_name)
write_list_to_file(filename, cars)