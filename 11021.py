# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyle, Feb 28 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 11021, BJ Online Judge
# https://www.acmicpc.net/problem/11021

import sys

t = int(input())

for loop in range(1,t+1):
    a, b = map(int,sys.stdin.readline().split())
    print('Case #%d:'%(loop), a + b)
    # print format, https://blockdmask.tistory.com/428, https://blog.naver.com/jnlovejy/221752289387

# END
 