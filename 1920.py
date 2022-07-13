# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1920, BJ Online Judge
# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

_ = int(input())
tmp = list(map(int, input().split()))
samples = {}
for x in tmp:
    samples[x] = 1
tmp.clear()

results = []
_ = int(input())
tmp = list(map(int, input().split()))
for x in tmp:
    if x in samples:
        results.append(1)
    else:
        results.append(0)

for x in results:
    print(x)