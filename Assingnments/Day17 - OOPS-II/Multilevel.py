class company:
    def __init__(self,companyname):
        self.companyname = companyname
class car(company):
    def __init__(self, companyname,cartype):
        super().__init__(companyname)
        self.cartype = cartype
class customer(car):
    def __init__(self, companyname, cartype, name):
        super().__init__(companyname, cartype)
        self.name = name
object = customer("BMW","X4 M","Kathirvel")
print(object.companyname)
print(object.name)
print(object.cartype)