# class variable: these are same for each instance
# https://www.youtube.com/watch?v=BJ-VvGyQxho&index=2&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
# 7:13 minutes
# difference btw 'Employee.raise_amt' & 'self.raise_amt' in methods. we can configure class variable for
#every instance if we use 'self'

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

print(Employee.num_of_emp)
emp1 = Employee('Abhi', 'Saharan', 80000)

# print(emp1.__dict__)
# print(Employee.__dict__)      #diff in Employee.amt_raise and self.amt_raise
# emp1.raise_amt = 1.05
# print(emp1.__dict__)

print(Employee.num_of_emp)