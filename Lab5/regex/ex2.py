import re

with open ("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.findall(r"аб{2,3}", file)
for i in a:
    print(i, end= " ")