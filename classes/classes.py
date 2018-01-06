# Python Object-oriented programming

# method: function associated with class
# instance variable: contains data that unique to each instance



class Employee:
    def __init__(self, first, last, pay):  # it initialize or call it constructor
        self.first = first  # all these are instance variables
        self.last = last
        self.pay = pay

    def email_set(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Abhi', 'Saharan', 80000)

print(emp1.fullname()) # in background it works like "Employee.fullname(emp1)" . Self means the object(emp1) got passed itself
