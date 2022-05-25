# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1316, BJ Online Judge
# https://www.acmicpc.net/problem/1316

n = int(input())
words = []
group_word_chk = 0

for cnt in range(n):
    words.append(input())

for cnt1 in range(n):
    if len(words[cnt1]) < 3 & len(words[cnt1]) > 0:
        group_word_chk += 1
    else:
        flag = True
        for cnt2 in range(len(words[cnt1])):
            for cnt3 in range(cnt2):
                if words[cnt1][cnt2] != words[cnt1][cnt2-1] and words[cnt1][cnt2] == words[cnt1][cnt3]:
                    flag = False
                    break
        if flag:
            group_word_chk += 1

print(group_word_chk)

# END
