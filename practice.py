#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sum1 = 0
n = 0
for l in a:
    sum1 += l[n]
    n += 1

sum2 = 0
m = 0
new_main = []
for l in a:
    new_list = l[-1::-1]
    new_main.append(new_list)
for i in new_main:
    sum2 += i[m]
    m += 1


print (abs(sum1 + sum2))

