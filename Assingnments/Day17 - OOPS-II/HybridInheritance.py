#single inheritance
class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def whoisthis(self):
        print(self.name,self.id)
class Employee(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def lpa(self):
        print("LPA:",self.salary*12)
class Department():
    def __init__(self,dept) -> None:
        self.dept = dept
    def department(self):
        print("Department:",self.dept)
class Developer(Employee,Department):
    def __init__(self, name, id, salary,dept,language):
        super().__init__(name, id, salary)
        Department.__init__(self,dept)
        self.language = language
    def developer(self):
        print("Name:",self.name)
        print("language:",self.language)
a = Developer("kathir",45,30000,"Web Development","Java")
a.whoisthis()
a.developer()
a.department()

