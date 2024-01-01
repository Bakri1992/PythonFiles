class Employee:
    raise_amount=1.05 # class attribute
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@gmail.com"
        self.pay=pay
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
class Developer(Employee):
    def __init__(self,first,last,pay,programminglan):
        super().__init__(first, last,pay)
        # OR this
        # Employee.__init__(self,first,last,pay)
        # it will pass first, last, pay to my Employee init method
        self.programminglan=programminglan
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp): # Add employee to my list
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):# Remove employee from my list
        if emp  in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:# Print all employee in my list
            print("-->",emp.fullname())


developer1=Developer("Bakri","Badet",50000,"C++")
developer2=Developer("Qais","Omar",70000,"Python")
# print(developer1.email)
# print(developer1.programminglan)
# print(developer1.pay)
# Manger1=Manager("Bakri","Badet",50000,["Omar","Soso"])
Manger2=Manager("Omar","Habibi",50000,[developer1])
# we passed in the list my object developer1 of my class Developer
# Manger1.print_emps()
Manger2.print_emps()
Manger2.add_emp(developer2) 
Manger2.print_emps()
