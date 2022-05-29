# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10250, BJ Online Judge
# https://www.acmicpc.net/problem/10250

t = int(input())

for cnt in range(t):
    h, w, n = map(int, input().split())

    room_h = n % h
    room_w = n // h

    if room_h > 0:
        room_w += 1
    else:
        room_h = h

    print(room_h * 100 + room_w)
