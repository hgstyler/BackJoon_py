# * ** * ** *** ** * ** *
# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1712, BJ Online Judge
# https://www.acmicpc.net/problem/1712

a,b,c = map(int,input().split())

if c - b <= 0: print(-1)
else: print(int(a / (c - b)) + 1)