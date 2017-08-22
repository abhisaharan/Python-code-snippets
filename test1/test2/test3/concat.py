def concat_str(x):
    new_list = []
    for letter in range(len(x)):
        slicing_x = x[0:letter + 1]
        new_list.append(slicing_x)
    return new_list


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return"My name is {}. I am {} years".format(self.name, self.age)


def kirupasir():
    print("we did it")
