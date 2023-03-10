s = input()
s1 = s[::-1]
if hash(s) == hash(s1):
    print('yes')
else:
    print('No')