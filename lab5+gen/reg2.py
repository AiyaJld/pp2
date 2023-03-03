import re
string=input()
match=re.findall("ab{2,3}", string)
print(match)