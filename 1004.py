# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1004, BJ Online Judge
# https://www.acmicpc.net/problem/1004

import sys
input = sys.stdin.readline

t = int(input())
res = []

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    routes = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        cond1 = (x - x1) ** 2 + (y - y1) ** 2
        cond2 = (x - x2) ** 2 + (y - y2) ** 2

        if (cond1 < r ** 2 and cond2 < r ** 2) or (cond1 > r ** 2 and cond2 > r ** 2):
            continue
        else:
            routes += 1

    res.append(routes)

for i in res:
    print(i)
# END