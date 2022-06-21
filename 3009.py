# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 3009, BJ Online Judge
# https://www.acmicpc.net/problem/3009

import sys
input = sys.stdin.readline
x_point = {}
y_point = {}

for i in range(3):
    x, y = map(int, input().split())

    if x in x_point:
        x_point[x] += 1
    else:
        x_point[x] = 1
    
    if y in y_point:
        y_point[y] += 1
    else:
        y_point[y] = 1

for i,j in x_point.items():
    if j == 1:
        print(i,end=' ')
        break

for i,j in y_point.items():
    if j == 1:
        print(i)
        break
