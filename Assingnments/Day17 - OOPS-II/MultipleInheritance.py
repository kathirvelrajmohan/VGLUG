class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Son(Father,Mother):
    def __init__(self,name):
        self.name = name
    def parents(self):
        print("Fathername:",self.fathername)
        print("Mothername:",self.mothername)

kathir = Son("kathirvel")
kathir.fathername = "Rajmohan"
kathir.mothername = "Amutha"
kathir.parents()
print(kathir.name)