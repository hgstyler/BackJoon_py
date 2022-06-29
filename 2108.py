# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2108, BJ Online Judge
# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

mean = round(sum(numbers) / n)

median = numbers[n // 2]

numbers_cnt = Counter(numbers).most_common()
print(numbers_cnt)
if len(numbers_cnt) > 1:
    if numbers_cnt[0][1] == numbers_cnt[1][1]:
        mode = numbers_cnt[1][0]
    else:
        mode = numbers_cnt[0][0]
else:
    mode = numbers_cnt[0][0]

ranges = numbers[-1] - numbers[0]

print(mean)
print(median)
print(mode)
print(ranges)
