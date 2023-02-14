class string():
    def __init__(self):
        self.str=""
    def getstr(self):
        self.str=input()
    def upper(self):
        print(self.str.upper())

str=string()
str.getstr()
str.upper()
