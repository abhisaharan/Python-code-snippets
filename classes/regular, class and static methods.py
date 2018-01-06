# regular method automatically takes instance as first argument

class Employee:
    num_of_emp = 0
    raise_amt = 1.04    # class variable
    def __init__(self, first, last, pay):  # it initialize or call it constructor
        self.first = first  # all these are instance variables
        self.last = last
        self.pay = pay
        Employee.num_of_emp += 1    # use case where we dont want to use self.class_variable. Number of employees need not
        # to be changed ever.

    def email_set(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)


emp1 = Employee('Abhi', 'Saharan', 80000)



