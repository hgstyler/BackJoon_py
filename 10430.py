# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 23 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 10430, BJ Online Judge
# https://www.acmicpc.net/problem/10430

A,B,C = map(int,input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
