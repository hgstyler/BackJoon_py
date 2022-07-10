# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 5086, BJ Online Judge
# https://www.acmicpc.net/problem/5086

import sys
input = sys.stdin.readline

n = 1
m = 1
result = []

while n != 0 and m != 0:
    n, m = map(int, input().split())

    if n < m and m % n == 0:
        result.append("factor")
    elif n > m and n % m == 0:
        result.append("multiple")
    elif n != 0 and m != 0:
        result.append("neither")

for i in result:
    print(i)