# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2908, BJ Online Judge
# https://www.acmicpc.net/problem/2908

a,b = map(str,input().split())

# type 1
# a = int(a[::-1])
# b = int(b[::-1])

# type 2
a = ''.join(reversed(a))
b = ''.join(reversed(b))

if a > b: print(a)
elif a < b: print(b)
