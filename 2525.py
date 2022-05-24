# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2525, BJ Online Judge
# https://www.acmicpc.net/problem/2525

hh, mm = map(int,input().split())
cooking_time = int(input())

hh_cook = int(cooking_time / 60)
mm_cook = int(cooking_time % 60)

hh_end = hh + hh_cook
mm_end = mm + mm_cook

if mm_end >= 60:
    hh_end = hh_end + int(mm_end / 60)
    mm_end = int(mm_end % 60)

if hh_end >=24:
    hh_end = hh_end - 24

# keep in mind '//' operator, which is not included in C++, https://www.programiz.com/python-programming/operators

print(hh_end, mm_end)

# END

