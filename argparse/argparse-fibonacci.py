import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        temp = a
        a = a + b
        b = temp
    return  b

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help='The fib number', type = int)

    args = parser.parse_args()
    result = fib(args.num)
    print("the"+str(args.num)+"th fib number is" + str(result))

if __name__ == 'main':
    Main()
