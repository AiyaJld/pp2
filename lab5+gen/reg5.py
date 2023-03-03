import re
string = input()
pattern =r"a.+b\b"
match=re.findall(pattern, string)
print(match)