# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1676, BJ Online Judge
# https://www.acmicpc.net/problem/1676

import sys
input = sys.stdin.readline

n = int(input())
res = 0

while n != 0:
    n //= 5
    res += n

print(res)

# END