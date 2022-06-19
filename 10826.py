# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10826, BJ Online Judge
# https://www.acmicpc.net/problem/10826

n = int(input())

fibo = []
fibo.append(int(0))
fibo.append(int(1))

for i in range(2, n + 1):
    fibo.append(fibo[i-2] + fibo[i-1])

print(fibo[n])