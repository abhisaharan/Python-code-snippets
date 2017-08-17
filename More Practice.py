def outer_func(message):

    def inner_func(msg):
        print(message)
        print(msg)
    return inner_func
a = outer_func("hii")
a("hi")
a("hello")
