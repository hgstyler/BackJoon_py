# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 8958, BJ Online Judge
# https://www.acmicpc.net/problem/8958

n = int(input())

for cnt in range(n):
    given_ox = input()
    len_ox = len(given_ox)
    sub_cnt = 1; main_cnt = 0
    for cnt2 in range(len_ox):
        if given_ox[cnt2] == 'X':
            sub_cnt = 1
        elif given_ox[cnt2] == 'O':
            main_cnt = main_cnt + sub_cnt
            sub_cnt = sub_cnt + 1
    print(main_cnt)

# END
