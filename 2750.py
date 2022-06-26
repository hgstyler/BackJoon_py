# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2750, BJ Online Judge
# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

for i in range(len(numbers)):
    print(numbers[i])
