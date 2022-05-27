# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1157, BJ Online Judge
# https://www.acmicpc.net/problem/1157

word = input().upper()

alpha_cnt = [0] * 26

for cnt in range(26):
    alpha_cnt[cnt] = word.count(chr(cnt+65))

if alpha_cnt.count(max(alpha_cnt)) > 1:
    print('?')
else:
    print(chr(alpha_cnt.index(max(alpha_cnt))+65))
