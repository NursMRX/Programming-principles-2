def spy_game(nums):
    seq = [0, 0, 7]
    idx = 0
    for num in nums:
        if num == seq[idx]:
            idx += 1
            if idx == 3:
                return True
    return False

numbers = list(map(int, input("Enter the elements of list: ").split()))
print(spy_game(numbers))