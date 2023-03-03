def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n=int(input())
l=[]
for i in even(n):
    l.append(str(i))
    
print(','.join(l))