# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2292, BJ Online Judge
# https://www.acmicpc.net/problem/2292

number = int(input())
a = 1
room = 1

if number == 1:
    print(number)
else:
    while number > a:
        a += 6 * room
        room += 1
    print(room)
