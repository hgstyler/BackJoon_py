# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 14681, BJ Online Judge
# https://www.acmicpc.net/problem/14681

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y < 0:
    print('3')
elif x < 0:
    print('2')
else:
    print('4')

# END
