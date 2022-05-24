# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2438, BJ Online Judge
# https://www.acmicpc.net/problem/2438

import sys

n = int(sys.stdin.readline())

for loop1 in range(1,n+1,1):
    for loop2 in range(1,loop1+1,1):
        print('*', end='')
        # print without '\n', https://angelplayer.tistory.com/106
    print('')

# END 

