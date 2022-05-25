# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11720, BJ Online Judge
# https://www.acmicpc.net/problem/11720

n = int(input())

# type 1
print(sum(map(int,input())))

# type 2
s = input()
sum = 0
for cnt in s:
    sum += int(cnt)
print(sum)

# type 3
s = input()
sum = 0
for cnt in range(n):
    sum += int(s[cnt])
print(sum)

# END
