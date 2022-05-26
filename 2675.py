# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2675, BJ Online Judge
# https://www.acmicpc.net/problem/2675

t = int(input())

for cnt0 in range(t):
    r,s = input().split()
    for cnt1 in range(0,len(s)):
        for cnt2 in range(int(r)):
            print(s[cnt1], end='')
    print()