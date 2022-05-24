# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 23 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2588, BJ Online Judge
# https://www.acmicpc.net/problem/2588

A = int(input())
B = int(input())

B_3 = B % 10
B_5 = int(B / 100)
B_4 = int((B - B_3 - B_5*100)/10)

multi_3 = A * B_3
multi_4 = A * B_4
multi_5 = A * B_5
multi_6 = A * B

print(multi_3)
print(multi_4)
print(multi_5)
print(multi_6)

