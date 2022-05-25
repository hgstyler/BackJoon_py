# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1065, BJ Online Judge
# https://www.acmicpc.net/problem/1065

def app():
    N = int(input())

    N_arr = [0] * 3;
    
    if N < 100:
        num_cnt = N
    elif N <= 101:
        num_cnt = 99
    elif N != 1000:
        num_cnt = 99
        
        for cnt in range(102, N+1):
            sub_cnt = 0

            cnt1 = cnt
            while cnt1 > 0:
                N_arr[sub_cnt] = cnt1 % 10
                cnt1 = int(cnt1 / 10)
                sub_cnt += 1

            d1 = N_arr[0] - N_arr[1]
            d2 = N_arr[1] - N_arr[2]

            if d1 == d2:
                num_cnt += 1
    else: num_cnt = 144

    print(num_cnt)

app()

# END
