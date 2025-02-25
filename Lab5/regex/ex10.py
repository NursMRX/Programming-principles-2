import re
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-ZА-Я])', '_', s).lower()
with open("row.txt", "r", encoding="utf-8") as row:
    file = row.read()
snake_case_string = camel_to_snake(file)
print(snake_case_string)