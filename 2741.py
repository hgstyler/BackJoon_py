# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyle, Feb 28 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2741, BJ Online Judge
# https://www.acmicpc.net/problem/2741

import sys

n = int(input())

for loop in range(1,n+1):
    a, b = map(int,sys.stdin.readline().split())
    # quick loading of 'input', https://bit.ly/3BZhQej
    print(a + b)

# END
 