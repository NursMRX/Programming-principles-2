import re
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.findall(r"[aа].*[бb]", file, re.IGNORECASE)
for i in a:
    print (i, end=";")