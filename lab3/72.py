list1=[1, 2, 3]
def sum_list(list1):
    y=0
    for i in list1:
        y+=i
    return y
x=lambda list1: sum_list(list1)
print(x(list1))