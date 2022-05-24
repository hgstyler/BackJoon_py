# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2753, BJ Online Judge
# https://www.acmicpc.net/problem/2753

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('1')
else:
    print('0')

# END
