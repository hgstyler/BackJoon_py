# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1037, BJ Online Judge
# https://www.acmicpc.net/problem/1037

import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

print(num_lst[0] * num_lst[n-1])

# END