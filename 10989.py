# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10989, BJ Online Judge
# https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

numbers = [0 for i in range(10001)]

n = int(input())

for i in range(n):
    tmp = int(input())
    numbers[tmp] += 1

for i in range(1, 10001):
    for j in range(numbers[i]):
        print(i)
