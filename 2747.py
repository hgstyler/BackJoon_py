# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2747, BJ Online Judge
# https://www.acmicpc.net/problem/2747

# Type1. simple version

import sys
# sys.setrecursionlimit(10 ** 6) # re-assign a recursive depth (default=1000), 10 ** 6 == int(1e6) https://fuzzysound.github.io/sys-setrecursionlimit
input = sys.stdin.readline

def fibo(n):
    first = 0
    second = 1

    for i in range(n):
        tmp = first

        first = second
        second = tmp + second

    return first

n = int(input())

print(fibo(n))


# Type 2. function memoization using lru-cache
'''
import sys
sys.setrecursionlimit(int(1e6)) # re-assign a recursive depth (default=1000), 10 ** 6 == int(1e6) https://fuzzysound.github.io/sys-setrecursionlimit

from functools import lru_cache # function memoization, memoization similar with caching https://ndb796.tistory.com/596
@lru_cache(maxsize=None)

def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input())

print(fibo(n) % 1000000)
'''

# Type 3. function memoization using functools.cache
'''
import sys
sys.setrecursionlimit(int(1e6)) # re-assign a recursive depth (default=1000), 10 ** 6 == int(1e6) https://fuzzysound.github.io/sys-setrecursionlimit

import functools # function caching, aka memoization https://docs.python.org/ko/3/library/functools.html
@functools.cache

def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input())

print(fibo(n) % 1000000)
'''

# Type 4. Basic concept of memoization
'''
import sys
sys.setrecursionlimit(int(1e6)) # re-assign a recursive depth (default=1000), 10 ** 6 == int(1e6) https://fuzzysound.github.io/sys-setrecursionlimit

class Fibo():
    def __init__(self):
        self.nums = {}

    def fibo(self, n):
        if n in [0, 1]: # same with 'if n == 0 or n == 1'
            return n
        elif n in self.nums:
            return self.nums[n]
        else:
            self.nums[n] = self.fibo(n - 1) + self.fibo(n - 2)
            return self.nums[n]

n = int(input())
f = Fibo()

print(f.fibo(n) % 1000000)
'''

# Type 5. Pisano Period
'''
import sys
input = sys.stdin.readline

mod = 1000000
p = mod // 10 * 15
fibo = [0, 1]

n = int(input())

for i in range(2, p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod

print(fibo[n%p])
'''