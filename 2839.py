# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2839, BJ Online Judge
# https://www.acmicpc.net/problem/2839

n = int(input())

num5 = n // 5

while num5 >= 0:
    if n % 5 == 0 or (n - num5 * 5) % 3 == 0:
        break
    else:
        num5 -= 1
num3 = (n - num5 * 5) // 3

if n == num5 * 5 + num3 * 3 and num5 >= 0:
    print(num5 + num3)
else:
    print(-1)