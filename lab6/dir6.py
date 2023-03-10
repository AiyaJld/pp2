import os

path = input()

try:
    os.chdir(path)
    for i in range(65, 91):
        a=open(chr(i)+'.txt', 'w')
except:
    pass