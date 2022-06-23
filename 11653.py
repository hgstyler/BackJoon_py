# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11653, BJ Online Judge
# https://www.acmicpc.net/problem/11653

n = int(input())
i = 2

if n != 1:
    while n != 1:
        if n % i == 0:
            print(i)
            n //= i
            if n % i != 0:
                i += 1
        else:
            i += 1
