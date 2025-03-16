# import re 
text = "sdfghfGemfkfmKefeafdfadfedfb"

# pattern = r"a.*b"

# a = re.split(r"(?=[A-ZА-Я])", text)

# for i in a:
#     print(i, end=" ")
import re
def spaces(text):
    res = ""
    pattern = re.compile(r"[a-zа-я\d]+|[A-ZА-Я][a-zа-я]*")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += " " + word
        else:
            res += word
    return res

a = spaces(text)
print(a)