# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 3036, BJ Online Judge
# https://www.acmicpc.net/problem/3036

import sys
input = sys.stdin.readline

def gcd(n1, n2):
    mod = n1 % n2

    while mod != 0:
        n1 = n2
        n2 = mod
        mod = n1 % n2

    return n2

n = int(input())

rings = list(map(int, input().split()))

ring1 = rings.pop(0)

for x in rings:
    print(f'{ring1 // gcd(ring1, x)}/{x // gcd(ring1, x)}')

# END