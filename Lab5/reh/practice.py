import re 
text = "sdfghf"
a = re.findall(r'[a-z]', text)
for i in a:
    print("_".join(a), end=" ")