# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1929, BJ Online Judge
# https://www.acmicpc.net/problem/1929

# Type 1.

import math
import sys

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if is_prime(i):
        print(i)

# Type 2. time over
'''
import math
import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    sqt = int(math.sqrt(i))
    if sqt == 1 and i != 1:
        print(i)
        continue
    else:
        if i % 2 == 1:
            for j in range(2, sqt + 1):
                if i % j == 0:
                    break
                elif j == sqt:
                    print(i)
'''