import re
string = input()
pattern="[a-z]+(?:_[a-z]+)+"
print(re.findall(pattern,string))