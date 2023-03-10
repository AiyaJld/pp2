import os

path = input()

try:
    os.chdir(path)
    f = input()
    a = open(f, 'w')
    a1 = a.write(str(list(map(int, input().split()))))
    a1.close()
except:
    pass