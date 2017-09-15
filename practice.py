import re


def fun(s):

    a = re.search(r'([\w]+)@([a-zA-Z0-9]+)\.([\w]{1,3})$', s)


    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)
    a = re.search(r'([\w]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{1,3})$', s)