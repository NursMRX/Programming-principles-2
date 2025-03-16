import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()

regex = re.split(r"(?=[A-ZА-Я])", file)
for i in regex:
    print (i, end=" ")