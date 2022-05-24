# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Feb 24 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 2884, BJ Online Judge
# https://www.acmicpc.net/problem/2884

hh, mm = map(int,input().split())

if hh == 0 and mm < 45:
    hh_alarm = 23
    mm_alarm = 60 - (45 - mm)
elif mm < 45:
    hh_alarm = hh -1
    mm_alarm = 60 - (45 - mm)
else:
    hh_alarm = hh
    mm_alarm = mm - 45

print(hh_alarm, mm_alarm)

# END
