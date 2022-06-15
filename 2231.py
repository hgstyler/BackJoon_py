# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2231, BJ Online Judge
# https://www.acmicpc.net/problem/2231

import sys
input = sys.stdin.readline

n = int(input())
m = n - 1
m_set = set()

while m >= 1:
    sub_sum = m
    i = m

    while i >= 1:
        sub_sum += int(i % 10)
        i /= int(10)

    if sub_sum == n:
        m_set.add(m)

    m -= 1

if len(m_set) == 0:
    print('0')
else:
    m_set = list(m_set)
    m_set.sort()
    print(m_set[0])
