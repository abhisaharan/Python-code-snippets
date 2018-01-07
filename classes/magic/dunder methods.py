
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

    def __repr__(self): # its for developers
        return  'Employee {} {} {}'.format(self.first, self.last, self.pay)

    def __str__(self): # its for end user
        return '{} {}'.format(self.fullname(), self.email_set())

    def __add__(self, other):
        return self.pay + other.pay

emp1 = Employee('Abhi', 'saharan', 90000)
emp2 = Employee('Edyta', 'Saharan', 90000)

#print(emp1.__repr__())
print(emp1) # it gives better representation of object now after modifying __repr__
print(emp1+emp2)    # using magic/dunder method