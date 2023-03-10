import os

path = input()

try:
    os.chdir(path)
    f = input()
    a = open(f, 'r')
    a1 = a.read().split("\n")

    print(len(a1))
except:
    print('ошибка')