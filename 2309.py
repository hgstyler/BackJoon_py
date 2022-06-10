# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2309, BJ Online Judge
# https://www.acmicpc.net/problem/2309

import sys
samples = []

for x in range(9):
    samples.append(int(input()))

samples.sort()

for i in range(9):
    for j in range(9):
        if j == i:
            continue
        else:
            sub_sum = sum(samples) - samples[i] - samples[j]
            if sub_sum == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(f'{samples[k]}')
                exit()