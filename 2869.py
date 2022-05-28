# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2869, BJ Online Judge
# https://www.acmicpc.net/problem/2869

a,b,v = map(int, input().split())

print(int((v - b - 1) / (a - b) + 1))