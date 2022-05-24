# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2480, BJ Online Judge
# https://www.acmicpc.net/problem/2480

# min, max, https://ddolcat.tistory.com/686

dice1, dice2, dice3 = map(int,input().split())

if dice1 == dice2 and dice1 == dice3:
    prize = 10000 + dice1 * 1000
elif dice1 == dice2:
    prize = 1000 + dice1 * 100
elif dice1 == dice3:
    prize = 1000 + dice1 * 100
elif dice2 == dice3:
    prize = 1000 + dice2 * 100
else:
    prize = max(dice1, dice2, dice3) * 100

print(prize)

# END

