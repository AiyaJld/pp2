def permutation(a):
    n=len(a)
    i=0
    j=0
    for i in range(n-2, -1, -1):
        if (a[i]<a[i + 1]):
            break
    if (i<0) : 
        a.reverse()
    else:
        for j in range(n-1, i, -1):
            if(a[j] > a[i]):
                break
        a[i], a[j] = a[j], a[i]

        start, end = i+1, len(a)

        a[start:end] = a[start:end][::-1]

def prmttn(a):
    a = sorted(a)
    b = sorted(a, reverse=True)

    while a != b:
        print(''.join(a))
        permutation(a)
    print(''.join(a))

a=str(input())
list1=list(a)
print(prmttn(list1))