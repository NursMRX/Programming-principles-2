def return_num(end_num):
    while end_num >= 0:
        yield end_num
        end_num -= 1

end_num = int(input("Enter a end_point number: "))
it = return_num(end_num)

for x in it:
    if x >= 0:
        print(x, end=' ')