# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1759, BJ Online Judge
# https://www.acmicpc.net/problem/1759

import sys

def gen_pw(pws):
    how_many_vows = 0
    for i in pws:
        if i in vowels:
            how_many_vows += 1
    if how_many_vows >= 1 and l - how_many_vows >= 2:
        print(''.join(pws))
 
def pw_checker(v, pws):
    if len(pws) == l:
        gen_pw(pws)
        return
    if v == c:
        return
    pws.append(alpha_list[v])
    pw_checker(v+1, pws)
    pws.pop()
    pw_checker(v+1, pws)

input = sys.stdin.readline

l, c = map(int, input().split())
alpha_list = sorted(input().split())
vowels = set(['a', 'e', 'i', 'o', 'u'])
 
pw_checker(0, [])