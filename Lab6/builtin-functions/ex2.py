def count(string1):
    lower = 0
    upper = 0
    for i in string1:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f"lower: {lower}")
    print(f"upper: {upper}")
string1 = input()
count(string1)