# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11651, BJ Online Judge
# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline

n = int(input())

point_list = []

for _ in range(n):
    point_list.append(list(map(int, input().split())))

point_list.sort(key=lambda x: (x[1], x[0]))

for i in point_list:
    print(f"{i[0]} {i[1]}")