# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 9020, BJ Online Judge
# https://www.acmicpc.net/problem/9020

import math
'''
def is_prime_num(n):
    arr = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1

    return [i for i in range(2, n+1) if arr[i]]
'''

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    n1 = int(n / 2)

    if is_prime(n1):
        print(f'{n1} {n1}')
    else:
        while n1 > 0:
            n1 -= 1
            if is_prime(n1) and is_prime(n-n1):
                print(f'{n1} {n-n1}')
                break
