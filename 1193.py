# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1193, BJ Online Judge
# https://www.acmicpc.net/problem/1193

n = int(input())
line_index = 1

while n > line_index:
    n -= line_index
    line_index += 1

if line_index % 2 == 0:
    print(f'{n}/{line_index + 1 -n}')
else:
    print(f'{line_index + 1 -n}/{n}')