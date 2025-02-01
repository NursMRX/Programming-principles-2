def UniqueCheck(list):
    unique_list = []
    unique_list.append(list[0])
    for num in list:
        if num in unique_list:
            continue
        else:
            unique_list.append(num)

    return unique_list

numbers = list(map(int, input("Enter an elements of list: ").split()))
print(UniqueCheck(numbers))