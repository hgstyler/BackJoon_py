# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1010, BJ Online Judge
# https://www.acmicpc.net/problem/1010

import sys
import math
input = sys.stdin.readline

t = int(input())
res = []

for _ in range(t):
    n, m = map(int, input().split())
    res.append(math.comb(m, n))

for i in res:
    print(i)
# END