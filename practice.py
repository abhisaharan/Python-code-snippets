#!/bin/python3

import sys
import re


n = int(input().strip())
binary_form = bin(n)
n_of_1 = 0
a = re.findall(r'[1]{1,}', binary_form)
print(a)

#print(n_of_1)