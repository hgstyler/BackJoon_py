# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10809, BJ Online Judge
# https://www.acmicpc.net/problem/10809

s = input()
lower_letter = [-1] * 26

for cnt in range(0,len(s)):
    for cnt1 in range(0, 26):
        if s[cnt] == chr(cnt1 + 97):
            if lower_letter[cnt1] == -1:
                lower_letter[cnt1] = cnt

for cnt in range(0,26):
    print(lower_letter[cnt], end=' ')
