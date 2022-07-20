# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1358, BJ Online Judge
# https://www.acmicpc.net/problem/1358

import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())

inside_cnt = 0
r = h // 2
x1 = x; y1 = y + r
x2 = x + w; y2 = y + r

for _ in range(p):
    x_player, y_player = map(int, input().split())

    d1 = (x_player - x1) ** 2 + (y_player - y1) ** 2
    d2 = (x_player - x2) ** 2 + (y_player - y2) ** 2
    cond1 = d1 <= r ** 2 or d2 <= r ** 2
    
    cond2_sub1 = x <= x_player <= x + w
    cond2_sub2 = y <= y_player <= y + h
    cond2 = cond2_sub1 and cond2_sub2

    if cond1 or cond2:
        inside_cnt += 1

print(inside_cnt)
# END