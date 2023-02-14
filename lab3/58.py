def has_33(n):
    for i in range(len(n) - 1):
        if(n[i] == 3 and n[i + 1] == 3):
            return True
    return False

list2 = list(map(int, input().split()))
print(has_33(list2))