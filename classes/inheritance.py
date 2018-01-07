#MRO:
#print(help(Developer)) # to check MRO, it helps or any child class name instead of Developer

class Employee:
    num_of_emp = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emp += 1


    def email_set(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # or Employee.__init__(self, first, last, pay) to access parent class variables
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None ):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev1 = Developer('Abhi', 'Saharan', 80000, 'Python')
dev2 = Developer('Edyta', 'Saharan', 90000, 'python')

mgr_1 = Manager('Su', 'smith', 90000, [dev1] )
print(mgr_1.email_set())
print(mgr_1.print_emp())
mgr_1.add_emp(dev2)
print(mgr_1.print_emp())

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))



#print(help(Developer)) # to check MRO, it helps

