# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1016, BJ Online Judge
# https://www.acmicpc.net/problem/1016

import sys
import math

def is_not_power(n):
    sub_cnt = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % pow(i,2) == 0:
            sub_cnt += 1
            break
    
    if (sub_cnt == 0):
        return True
    else:
        return False

m1, m2 = map(int, sys.stdin.readline().split())
main_cnt = 0

for i in range(m1, m2 + 1):
    main_cnt += is_not_power(i)

print(main_cnt)
