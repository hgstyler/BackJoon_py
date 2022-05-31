# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2775, BJ Online Judge
# https://www.acmicpc.net/problem/2775

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    room = []

    room.append(0)
    room[0] = []
    for cnt1 in range(n + 1):
        room[0].append(cnt1)

    for cnt1 in range(1, k + 1):
        room.append(cnt1)
        room[cnt1] = []
        room[cnt1].append(0)
        for cnt2 in range(1, n + 1):
            sub_sum = 0
            for cnt3 in range(1, cnt2 + 1):
                sub_sum += room[cnt1 - 1][cnt3]
            room[cnt1].append(sub_sum)

    print(room[k][n])
    room.clear()