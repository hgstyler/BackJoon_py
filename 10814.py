# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10814, BJ Online Judge
# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

n = int(input())
members = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    members.append([age, name]) # FYI, (age, name) tuple, [age, name] list

members.sort(key = lambda x : x[0])

for i in members:
    print(i[0], i[1])