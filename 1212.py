# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1212, BJ Online Judge
# https://www.acmicpc.net/problem/1212

oct_num = input()
oct_table = [ "000","001","010","011","100","101","110","111" ]
zero_bool = False

for i in range(len(oct_num)):
    digit = ord(oct_num[i]) - ord('0')
    if i == 0:
        if digit == 0:
            continue
        elif digit == 1:
            print("1",end='')
            zero_bool = True
            continue
        elif digit == 2:
            print("10",end='')
            zero_bool = True
            continue
        elif digit == 3:
            print("11",end='')
            zero_bool = True
            continue
        else:
            print(oct_table[digit], end='')
            if oct_table[digit] != "000":
                zero_bool = True
            continue
    else:
        print(oct_table[digit], end='')
        if oct_table[digit] != "000":
                zero_bool = True
        continue

if zero_bool == False:
    print("0")