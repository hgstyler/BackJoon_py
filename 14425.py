# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 14425, BJ Online Judge
# https://www.acmicpc.net/problem/14425

import sys

n, m = map(int, sys.stdin.readline().split())
sample_list = set()
checker = 0

for i in range(n):
    sample_list.add(sys.stdin.readline())

for i in range(m):
    if sys.stdin.readline() in sample_list:
        checker += 1

print(checker)

# END