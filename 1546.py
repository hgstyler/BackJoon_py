# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 1546, BJ Online Judge
# https://www.acmicpc.net/problem/1546

N = int(input())
scores = [0] * N # List vs Array https://velog.io/@ayoung0073/python-list

scores = list(map(int, input().split()))
max_value = max(scores)

for cnt in range(N):
    scores[cnt] = scores[cnt] / max_value * 100

avg_score = sum(scores) / N

print(avg_score)

# END
