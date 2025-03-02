def polindrome(string):
    if string == reversed(string):
        print("Polindrome")
    else:
        print("Not polindrome")
    
string = input()
polindrome(string)