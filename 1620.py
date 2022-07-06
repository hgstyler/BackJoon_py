# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1620, BJ Online Judge
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poke = {}
ans = []

for i in range(1, n + 1):
    tmp1 = input().rstrip()
    tmp2 = str(i)
    poke[tmp1] = tmp2
    poke[tmp2] = tmp1

for _ in range(m):
    tmp1 = input().rstrip()
    ans.append(poke[tmp1])

for i in ans:
    print(i)