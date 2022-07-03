# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1181, BJ Online Judge
# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input())

words_lst = []

for _ in range(n):
    words_lst.append(input().rstrip())

words_lst = list(set(words_lst))

words_lst.sort()
words_lst.sort(key = len)

for i in words_lst:
    print(i)