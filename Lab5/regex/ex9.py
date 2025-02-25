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
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = spaces(file)
print(a)