def fib(n):
    a = 0
    b = 1
    for i in range(n):
        temp = b
        b = a+b
        a = temp
        #a, b = b, a+b
        print(a)

print(fib(10)mm