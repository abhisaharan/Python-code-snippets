from contextlib import contextmanager
import os

# cwd = os.getcwd()
# os.chdir("dir1")
# print(os.listdir())
# os.chdir(cwd)
#
# cwd = os.getcwd()
# os.chdir("dir2")
# print(os.listdir())
# os.chdir(cwd)

#instead of above code use context manager below

@contextmanager
def chg_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with chg_dir('dir1'):
    print(os.listdir())

with chg_dir('dir2'):
    print(os.listdir())
