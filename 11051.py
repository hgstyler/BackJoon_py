# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11051, BJ Online Judge
# https://www.acmicpc.net/problem/11051

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

res = 1
for i in range(k):
    res *= n
    n -= 1

div = 1
for i in range(2, k + 1):
    div *= i

print((res // div) % 10007)

# END