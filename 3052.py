# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 3052, BJ Online Judge
# https://www.acmicpc.net/problem/3052

numbers = [0,0,0,0,0,0,0,0,0,0]
main_cnt = 0

for cnt in range(0,10):
    numbers[cnt] = int(input())
    numbers[cnt] = int(numbers[cnt] % 42)

for cnt1 in range(0,10):
    dup_cnt = 0

    for cnt2 in range(cnt1+1,10):
        if numbers[cnt1] == numbers[cnt2]:
            dup_cnt = dup_cnt + 1

    if dup_cnt == 0:
        main_cnt = main_cnt + 1

print(main_cnt)
# END
