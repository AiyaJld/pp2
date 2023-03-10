import os

path = input()

try:
    os.chdir(path)
    d = os.listdir(os.getcwd())
    for i in d:
        if os.path.isdir(i):
            print('DIR ', i)
        elif os.path.isfile(i):
            print('FILE ', i)
except:
    print('нет такой папки')