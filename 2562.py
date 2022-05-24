# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2562, BJ Online Judge
# https://www.acmicpc.net/problem/2562

numbers = []

for cnt1 in range(9):
    numbers.append(int(input()))

max_number = 0
max_index = 0

for cnt2 in range(9):
    if numbers[cnt2] > max_number:
        max_number = numbers[cnt2]
        max_index = cnt2 + 1

print(max_number)
print(max_index)

# END
