class d():
    def __init__(self, length, width):
        self.len=length
        self.width=width
    def area(self):
        return self.len*self.width

a=int(input())
b=int(input())
c=d(a,b)
print(c.area())