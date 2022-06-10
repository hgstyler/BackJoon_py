# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1759, BJ Online Judge
# https://www.acmicpc.net/problem/1759

import sys

def be_encryped(cand):
    picked = []

    for i1 in range(0, l):
        picked.append(cand[i1])
        for i2 in range(i1 + 1, l + 1):
            picked.append(cand[i2])
            for i3 in range(i2 + 1, l + 2):
                picked.append(cand[i3])
                for i4 in range(i3 + 1, l + 3):
                    picked.append(cand[i4])

    return picked

def alpha_check(cand):
    sub_cnt = 0

    for ii in range(len(cand)):
        if cand[ii] == 'a' or cand[ii] == 'e' or cand[ii] == 'i' or cand[ii] == 'o' or cand[ii] == 'u':
            sub_cnt += 1

    if sub_cnt == 1 or sub_cnt == 2:
        return True
    else:
        return False

l,c = map(int, sys.stdin.readline().split())
candidates = []
passwd = []

candidates = list(sys.stdin.readline().split())
print(candidates)

candidates = [ord(x) for x in candidates]
print(candidates)

candidates.sort()
print(candidates)

candidates = [chr(x) for x in candidates]
print(candidates)

passwd = be_encryped(candidates)

for i in passwd:
    if alpha_check(i):
        print(i)
