# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1436, BJ Online Judge
# https://www.acmicpc.net/problem/1436

n = int(input())
i = 666; how_many_666 = 0

while how_many_666 <= 10000:
    if '666' in str(i):
        how_many_666 += 1
    if how_many_666 == n:
        print(i)
        break

    i += 1

# END