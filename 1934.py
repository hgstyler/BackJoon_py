# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1934, BJ Online Judge
# https://www.acmicpc.net/problem/1934

import sys
input = sys.stdin.readline

def gcd(n1, n2):
    mod = n1 % n2

    while mod != 0:
        n1 = n2
        n2 = mod
        mod = n1 % n2

    return n2

def lcm(n1, n2):
    return (n1 * n2) // gcd(n1, n2)

t = int(input())
res = []

for _ in range(t):
    num1, num2 = map(int, input().split())
    res.append(lcm(num1, num2))

for i in res:
    print(i)

# END