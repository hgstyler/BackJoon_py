# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 7568, BJ Online Judge
# https://www.acmicpc.net/problem/7568

# type 1. not Class used
'''
import sys
input = sys.stdin.readline

n = int(input())
weight = []
height = []

for i in range(n):
    tmp1, tmp2 = map(int, input().split())
    weight.append(tmp1)
    height.append(tmp2)

for i in range(n):
    rank = 1
    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            rank += 1
    print(rank, end=' ')
'''

# type 2. Class used
import sys
input = sys.stdin.readline

class Info:
    def __init__(self, w, h, r):
        self.weight = w
        self.height = h
        self.ranking = r

n = int(input())
people = []

for i in range(n):
    tmp1, tmp2 = map(int, input().split())
    info = Info(tmp1, tmp2, 1)
    people.append(info)

for i in range(n):
    for j in range(n):
        if people[i].height < people[j].height and people[i].weight < people[j].weight:
            people[i].ranking += 1
    print(people[i].ranking, end=' ')