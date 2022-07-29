# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 9375, BJ Online Judge
# https://www.acmicpc.net/problem/9375

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
fashion_item = []
res = []

for i in range(n):
    nn = int(input())

    for j in range(nn):
        _, y = input().split()
        fashion_item.append(y)
        
    fashion_cnt = Counter(fashion_item)
    cnt = 1

    for x in fashion_cnt:
        cnt *= fashion_cnt[x] + 1

    res.append(cnt - 1)
    fashion_item.clear()

for i in res:
    print(i)
# END