# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1016, BJ Online Judge
# https://www.acmicpc.net/problem/1016

import sys
import math

min_value, max_value = map(int, sys.stdin.readline().split())
none_sqrt_numbers = [False] * 1000001
last_sqrted_number = int(math.ceil(math.sqrt(float(max_value))))
cnt = 0

for i in range(2, last_sqrted_number + 1, 1):
    powered_number = int(math.pow(i, 2))
    sth_integer = int(math.ceil(float(min_value) / float(powered_number))) * powered_number

    if sth_integer > max_value:
        continue

    for j in range(sth_integer, max_value + 1, powered_number):
        none_sqrt_numbers[j - min_value] = True

for i in range(0, max_value - min_value + 1, 1):
    if none_sqrt_numbers[i] is False:
        cnt += 1

print(cnt)