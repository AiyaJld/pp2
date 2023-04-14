import os

path = input()

try:
    os.chdir(path)
    f1 = input()
    path2 = input()
    f2 = input()
    with open(f1,'r') as input, open(path2 + '/' + f2, 'a') as output:
        for line in input:
            output.write(line)
except:
    pass