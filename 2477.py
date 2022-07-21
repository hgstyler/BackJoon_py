# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2477, BJ Online Judge
# https://www.acmicpc.net/problem/2477

import sys
input = sys.stdin.readline

k = int(input())
melon_field = []
len_EW = 0; len_NS = 0

for i in range(6):
    melon_field.append(list(map(int, input().split())))
    if melon_field[i][0] <= 2:
        len_EW += melon_field[i][1]
    else:
        len_NS += melon_field[i][1]

len_EW = len_EW // 2; len_NS = len_NS // 2

for i in range(6):
    if i < 5:
        cond = bool(melon_field[i][1] == len_EW or melon_field[i][1] == len_NS) and (melon_field[i + 1][1] == len_EW or melon_field[i + 1][1] == len_NS)
        if cond:
            target_index = i + 1
            break
    else:
        cond = bool(melon_field[i][1] == len_EW or melon_field[i][1] == len_NS) and (melon_field[0][1] == len_EW or melon_field[0][1] == len_NS)
        if cond:
            target_index = 0
            break

x_iter = target_index + 2
if x_iter >= 6:
    x_iter -= 6
y_iter = target_index + 3
if y_iter >= 6:
    y_iter -= 6

print((len_EW * len_NS - melon_field[x_iter][1] * melon_field[y_iter][1]) * k)

# END