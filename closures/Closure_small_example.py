def outer_func(message):

    def inner_func(msg):
        print(message)
        print(msg)
    return inner_func
a = outer_func("hii")
a("hi")  # if you do a.__name__ you will find that "a" is inner_func
a("hello")
