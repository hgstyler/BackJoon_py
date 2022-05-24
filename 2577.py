# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2577, BJ Online Judge
# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

res = a * b * c
num_cnt = [0,0,0,0,0,0,0,0,0,0]
cnt = res

while cnt > 0:
    num_cnt[int(cnt % 10)] = num_cnt[int(cnt % 10)] + 1
    cnt = int(cnt / 10)

for cnt2 in range(0,10):
    print(num_cnt[cnt2])

# END
