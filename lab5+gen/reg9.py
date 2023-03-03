import re
s = input()
s = ' '.join(re.findall("[A-Z][a-z]+", s))
print(s)
