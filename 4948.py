# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 4948, BJ Online Judge
# https://www.acmicpc.net/problem/4948

import sys
import math

prime_number = []

for i in range(2, 246913):
    sub_cnt = 0

    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            sub_cnt += 1
            break

    if sub_cnt == 0:
        prime_number.append(i)

while True:
    n = int(sys.stdin.readline())
    n2 = 2 * n
    cnt = 0

    if n:
        for i in prime_number:
            if n < i <= n2:
                cnt += 1

        print(cnt)
    else:
        break
