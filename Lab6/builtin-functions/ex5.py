def check_all_true(tuple):
    return all(tuple)


tuple1 = (True, 1, 'McLaren')
tuple2 = ('Maybach', ' ', 0)

print(check_all_true(tuple1))
print(check_all_true(tuple2))