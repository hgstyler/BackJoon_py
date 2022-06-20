# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11444, BJ Online Judge
# https://www.acmicpc.net/problem/11444

import sys
sys.setrecursionlimit(int(1e6)) # re-assign a recursive depth (default=1000), 10 ** 6 == int(1e6) https://fuzzysound.github.io/sys-setrecursionlimit
input = sys.stdin.readline

# https://www.acmicpc.net/blog/view/28

CONST_MOD = 1000000007

fibo = [0, 1]

n = int(input())

for i in range(2, n + 1):
    fibo.append((fibo[i-1] + fibo[i-2]) % CONST_MOD)

print(fibo[n])