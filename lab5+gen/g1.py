def sq(n):
    for i in range(n+1):
        yield i**2

class Squares:
    def __init__(self, n):
        self.cur = 1
        self.end_point = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur ** 2 > self.end_point:
            raise StopIteration()
        self.cur += 1
        return (self.cur - 1) ** 2

n=int(input())
for i in Squares(n):
    print(i)