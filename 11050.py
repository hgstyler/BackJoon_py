# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11050, BJ Online Judge
# https://www.acmicpc.net/problem/11050

import sys
input = sys.stdin.readline

def fact(n):
    if n != 0 and n != 1:
        return fact(n - 1) * n
    else:
        return 1

n, k = map(int, input().split())

print(fact(n) // fact(k) // fact(n - k))