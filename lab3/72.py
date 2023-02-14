class s:
    def __init__(self, sd):
        self.sd = sd
    def rev(self):
        print(self.sd [::-1])

z = s(str(input()))
z.rev()

class string():
    def __init__(self, string1):
        self.string=string1
    def getstr(self, string1):
        print(len(self.string))

s=str(input())
s1=string(s)
s1.getstr(s)

