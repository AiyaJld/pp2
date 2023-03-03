import re
s = input()
s1 = re.findall("[a-z]+", s)
s1 = s1[0]
s = re.findall("[A-Z][^A-Z]*", s)
s = [i.lower() for i in s]
s.insert(0, s1)
s = '_'.join(s)
print(s)
