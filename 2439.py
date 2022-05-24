# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2439, BJ Online Judge
# https://www.acmicpc.net/problem/2439

import sys

n = int(sys.stdin.readline())

for loop1 in range(1,n+1,1):
    print(' '*(n-loop1)+'*'*loop1)
    # 3 types of right-sided '*', https://codingpractices.tistory.com/38

# END 
