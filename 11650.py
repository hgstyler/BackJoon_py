# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11650, BJ Online Judge
# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

n = int(input())

point_list = []

for _ in range(n):
    point_list.append(list(map(int, input().split())))

point_list.sort(key=lambda x: (x[0], x[1]))
# 'key=lambda' for sort() https://kingofbackend.tistory.com/98

for i in point_list:
    print(f"{i[0]} {i[1]}")