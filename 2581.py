# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2581, BJ Online Judge
# https://www.acmicpc.net/problem/2581

import math

def prime_num(m, n):
    arr = [True for i in range(n + 1)]
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1

    return [i for i in range(m, n+1) if arr[i]]

m = int(input())
n = int(input())

if len(prime_num(m, n)) != 0:
    print(sum(prime_num(m, n)))
    print(min(prime_num(m, n)))
else:
    print(-1)