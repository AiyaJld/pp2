class shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class square():
    def __init__(self, length):
        self.len=length
    def area(self):
        return self.len**2
    
a=square(int(input()))
print(a.area())


