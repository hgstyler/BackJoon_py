# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1269, BJ Online Judge
# https://www.acmicpc.net/problem/1269

import sys
input = sys.stdin.readline

_, _ = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

# set 1 https://pybasall.tistory.com/94
# set 2 https://pybasall.tistory.com/93
print(len(set_a ^ set_b))