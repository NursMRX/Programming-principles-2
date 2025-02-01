def histogram(list):
    for num in list:
        print('*' * num)

nums = list(map(int, input("Enter an elements of list: ").split()))
histogram(nums)