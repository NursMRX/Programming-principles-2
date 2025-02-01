def checkPalindrome(string):
    new_string = ''.join(ch.lower() for ch in string if ch.isalnum())
    if new_string == new_string[::-1]:
        return "YES"
    else:
        return "NO"

string = str(input("Enter a word/sentence: "))
print(checkPalindrome(string))