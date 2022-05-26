# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1157, BJ Online Judge
# https://www.acmicpc.net/problem/1157

word = input()

alpha_cnt = [0] * 26

for cnt1 in range(len(word)):
    for cnt2 in range(26):
        if word[cnt1] == chr(alpha_cnt[cnt2] + 65):
            alpha_cnt[cnt2] += 1

print(alpha_cnt)

for cnt1 in range(0,len(word)):
    for cnt2 in range(26):
        if word[cnt1] == chr(alpha_cnt[cnt2] + 97):
            alpha_cnt[cnt2] += 1

sub_cnt = 0
for cnt in range(26):
    if alpha_cnt[cnt] == max(alpha_cnt):
        sub_cnt += 1

if sub_cnt == 1:
    print(alpha_cnt.index(max(alpha_cnt)) + 65)
else:
    print('?')
