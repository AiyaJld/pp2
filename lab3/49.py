class Point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x+=x
        self.y+=y

    def dist(self, point1):
        x1=point1.x-self.x 
        y1=point1.y-self.y
        return (x1**2+y1**2)**0.5

a1=Point(float(input()), float(input()))
a2=Point(float(input()), float(input()))
print(a1.show())
print(a2.show())
a1.move(float(input()), float(input()))

print(a1.show())
print(a1.dist(a2))