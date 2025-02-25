import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.sub(r"[ ,.]", ":", file)
for i in a:
    print(i, end=" ")