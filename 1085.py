# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1085, BJ Online Judge
# https://www.acmicpc.net/problem/1085

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
distance = []

distance.append(abs(x))
distance.append(abs(y))
distance.append(abs(w - x))
distance.append(abs(h - y))

distance.sort()

print(distance[0])