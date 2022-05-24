# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyle, Feb 28 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 15552, BJ Online Judge
# https://www.acmicpc.net/problem/15552

import sys

t = int(input())

for loop in range(1,t+1):
    a, b = map(int,sys.stdin.readline().split())
    # quick loading of 'input', https://bit.ly/3BZhQej
    print(a + b)

# END
 