# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1018, BJ Online Judge
# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
paint_bw = set()
paint_wb = set()

for i in range(n):
    board.append(input().rstrip())

for n_axis in range(0, n - 8 + 1, 1):
    for m_axis in range(0, m - 8 + 1, 1):
        tmp_bw = 0
        tmp_wb = 0
        for i in range(8):
            for j in range(8):
                if (j % 2 == 0 and i % 2 == 0) or (j % 2 != 0 and i % 2 != 0):
                    if board[i + n_axis][j + m_axis] != 'B':
                        tmp_bw += 1
                    else:
                        tmp_wb += 1
                else:
                    if board[i + n_axis][j + m_axis] != 'W':
                        tmp_bw += 1
                    else:
                        tmp_wb += 1
        paint_bw.add(tmp_bw)
        paint_wb.add(tmp_wb)

paint_bw = list(paint_bw)
paint_wb = list(paint_wb)

paint_bw.sort()
paint_wb.sort()

if paint_bw[0] < paint_wb[0]:
    print(paint_bw[0])
else:
    print(paint_wb[0])