def prime(n):
    if n==1: 
        return False
    if n==2: 
        return True
    if n%2==0: 
        return False
    else:
        a=int(n**0.5)+1
        for i in range(3, a+1):
            if i%2==0:
                return False
            else:
                return True
    
def filter_prime(list):
    list1=[]
    for i in list:
        if (prime(i)==True):
            list1.append(i)
        
    return list1

list2 = list(map(int, input().split()))

print(filter_prime(list2))