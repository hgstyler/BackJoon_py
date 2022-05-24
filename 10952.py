# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Mar 3 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 10952, BJ Online Judge
# https://www.acmicpc.net/problem/10952

a = int(1); b = int(1)
condition = bool(1)

while condition:
    a, b = map(int, input().split())
    condition = not (a == 0 and b == 0)
    if not condition:
        break
    print(a + b)

# END


