# https://www.youtube.com/watch?v=jCzT9XFZ5bw


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):        # we are defining email method but down we are accessing it like a attribute "emp_1.email"
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter # setter attribute used . After
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter  # setter attribute used . After
    def fullname(self):
        self.first = None
        self.last = None



emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Abhi saharan'

print(emp_1.first)
print(emp_1.email)  # this is due to property decorator without decorator we have to write emp_1.email()
print(emp_1.fullname)



