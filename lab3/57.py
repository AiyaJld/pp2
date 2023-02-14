def reverse_w(a):
    a=a.split()
    a.reverse()
    return  ' '.join(a)

k=str(input())
print(reverse_w(k))