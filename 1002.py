# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1002, BJ Online Judge
# https://www.acmicpc.net/problem/1002

import sys
input = sys.stdin.readline
import math

t = int(input())
res = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d == 0 and r1 == r2:
        res.append(-1)
    elif abs(r1 - r2) == d or r1 + r2 == d:
        res.append(1)
    elif abs(r1 - r2) < d < r1 + r2:
        res.append(2)
    else:
        res.append(0)

for i in res:
    print(i)

# END