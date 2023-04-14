import os

path = input()

try:
    os.chdir(path)
    print(os.access(path, os.F_OK))
except:
    pass

try:
    os.chdir(path)
    print(os.access(path, os.R_OK))
except:
    pass

try:
    os.chdir(path)
    print(os.access(path, os.W_OK))
except:
    pass

try:
    os.chdir(path)
    print(os.access(path, os.X_OK))
except:
    pass