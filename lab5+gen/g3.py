def div(n):
    for i in range(0, n+1, 12):
                yield i

n= int(input())
for i in div(n):
    print(i)