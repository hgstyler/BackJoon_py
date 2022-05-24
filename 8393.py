# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyle, Feb 28 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 8393, BJ Online Judge
# https://www.acmicpc.net/problem/8393

n = int(input())
sum = 0
# runtime error caution, declare an initial sum, https://www.acmicpc.net/board/view/52969

for loop in range(1,n+1):
    sum = sum + loop

print(sum)

# END
 