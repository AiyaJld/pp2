import math
n=int(input("number of sides: "))
l=float(input("length of a side: "))
a=(n/4)*math.pow(l,2)*(math.cos(math.pi/n)/math.sin(math.pi/n))
print(a)