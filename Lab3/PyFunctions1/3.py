def solve(numheads, numlegs):
    # x + y = numheads
    # 2x + 4y = numlegs
    
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    
    if y.is_integer() and x >= 0 and y >= 0:
        return int(x), int(y)
    else:
        return "No solution"

print(solve(35, 94))