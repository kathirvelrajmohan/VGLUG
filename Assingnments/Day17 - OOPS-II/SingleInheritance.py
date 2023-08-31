class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printDetails(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self, name, age, standard, section):
        super().__init__(name, age)
        self.standard = standard
        self.section = section 
    def printDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Standard:",self.standard)
        print("Section:",self.section)
a = Student("kathirvel",20,"CSE","C")
b = Student("Thariq",25,"ECE","B")
a.printDetails()
b.printDetails()