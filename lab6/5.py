def f(x):
    if x == "True":
        return True
    return False
    
a = [f(x) for x in input().split()]
x = all(a)
print(x)