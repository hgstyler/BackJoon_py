# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 4673, BJ Online Judge
# https://www.acmicpc.net/problem/4673

def app():
    all_numbers = [1] * 10000

    for cnt in range(10000):
        sub_num = cnt + 1
        sub_sum = cnt + 1

        while sub_num > 0:
            sub_sum = int(sub_sum + sub_num % 10)
            sub_num = int(sub_num / 10)
        if sub_sum <= 10000:
            all_numbers[int(sub_sum - 1)] = 0

    for cnt in range(10000):
        if all_numbers[cnt - 1] == 1:
            print(cnt)

app()

# END
