s = input()
lower = []
for i in s:
        if str(i).islower():
            lower.append(1)
upper = []
for i in s:
        if str(i).isupper():
            upper.append(1)

    
print('lower',sum(lower))
print('upper',sum(upper))