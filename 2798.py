# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2798, BJ Online Judge
# https://www.acmicpc.net/problem/2798

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
blackjack = list(map(int, input().split()))
sum_jack = set()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if k == i or k == j:
                continue
            if blackjack[i] + blackjack[j] + blackjack[k] > m:
                continue
            else:
                sum_jack.add(blackjack[i] + blackjack[j] + blackjack[k])

sum_jack = list(sum_jack)
sum_jack.sort()
sum_jack.reverse()

print(sum_jack[0])