# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1764, BJ Online Judge
# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = {}
dbj_people = []

for _ in range(n + m):
    tmp = input().rstrip()
    if tmp in people:
        people[tmp] += 1
    else:
        people[tmp] = 1
    
    if tmp in people and people[tmp] > 1:
        dbj_people.append(tmp)

dbj_people.sort()

print(len(dbj_people))
for i in dbj_people:
    print(i)