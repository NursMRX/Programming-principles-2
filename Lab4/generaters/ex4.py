def squares(start_num, end_num):
    for num in range(start_num, end_num + 1):
        yield num ** 2

start_num = int(input("Enter the number: "))
end_num = int(input("Enter the number: "))

it = squares(start_num, end_num)

for x in it:
    print(x, end=' ')

# for i in it:
#     print(i, end="")
#     if i != end_num**2:
#         print(", ", end="")