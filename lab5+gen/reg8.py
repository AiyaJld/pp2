import re
s = input()
s=re.findall('[A-Z]', s)
ans=''.join(s)
print(ans)