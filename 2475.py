# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2475, BJ Online Judge
# https://www.acmicpc.net/problem/2475

import sys
input = sys.stdin.readline

tmp = [x ** 2 for x in map(int, input().split())]

print(sum(tmp) % 10)

# END
