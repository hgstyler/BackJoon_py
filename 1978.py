# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1978, BJ Online Judge
# https://www.acmicpc.net/problem/1978

import math

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

prime_counter = 0

n = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    prime_counter += is_prime(i)

print(prime_counter)
