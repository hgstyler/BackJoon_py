# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 18870, BJ Online Judge
# https://www.acmicpc.net/problem/18870

import sys

n = int(input())

arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(list(set(arr1)))
dic1 = {arr2[i]:i for i in range(len(arr2))}

for i in arr1:
    print(dic1[i], end=' ')

# END