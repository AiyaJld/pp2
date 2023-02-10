class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

p1.age=40
print(p1.age)

del p1.age
print(p1.age)