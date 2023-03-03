import re
string = input()
pattern="[A-Z][a-z]+"
print(re.findall(pattern,string))