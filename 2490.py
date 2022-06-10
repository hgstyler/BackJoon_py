# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2490, BJ Online Judge
# https://www.acmicpc.net/problem/2490

import sys

for i in range(3):
    sum_atod = 0
    a, b, c, d = map(int, sys.stdin.readline().split())
    sum_atod = a + b + c + d

    if sum_atod == 1:
        print('C')
    elif sum_atod == 2:
        print('B')
    elif sum_atod == 3:
        print('A')
    elif sum_atod == 4:
        print('E')
    else:
        print('D')