# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2447, BJ Online Judge
# https://www.acmicpc.net/problem/2447

import sys
sys.setrecursionlimit(10 ** 6) # https://fuzzysound.github.io/sys-setrecursionlimit
input = sys.stdin.readline

def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

n = int(input())

print('\n'.join(star(n)))