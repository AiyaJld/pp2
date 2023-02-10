class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    self.firstname=fname
    self.lastname=lname
x = Student("Mike", "Olsen")
x.printname()
