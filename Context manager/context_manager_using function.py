from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        f = open(filename, mode)    #setup code
        yield f
    finally:
        f.close()   #teardown code

with open_file("another_sample.txt", 'w') as p:
    p.write("testing again")

print(p.closed)