import re
string=input()
match=re.findall("ab*", string)
print(match)