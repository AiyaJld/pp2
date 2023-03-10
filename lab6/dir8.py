import os

path = input()

try:
    os.chdir(path)
    f = input()
    if os.access(f, os.W_OK):
        os.remove(f)
    else:
        print('нет доступа')
except:
    pass