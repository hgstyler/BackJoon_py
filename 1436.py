# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1436, BJ Online Judge
# https://www.acmicpc.net/problem/1436

n = input()
i = 1; how_many_666 = 0

while how_many_666 <= 10000:
    number = str(i)
    if len(number) <= 3:
        for riter in iter(reversed(number)):
            if (riter == '6' and next(riter) == '6' and next(next(riter)) == '6'):
                how_many_666 += 1
                break

    if how_many_666 is n:
        print(i)
        break

    i += 1

# END