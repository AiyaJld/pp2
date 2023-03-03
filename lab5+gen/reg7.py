import re
s = input()
#s=s.split('_')
"""for i in range(0, len(s)):

    x=re.sub("_", "", s[i])
    x=re.sub(s[i], s[i].upper(), s[i])

print(x)
"""

s1 = s.upper()
camel = ''
i = 0
while(i != len(s)):
    if s[i] == '_':
        camel += s[i] + s1[i+1]
        i += 2
    else:
        camel += s[i]
        i += 1
camel = re.sub('_', '', camel)
print(camel)