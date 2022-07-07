# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10816, BJ Online Judge
# https://www.acmicpc.net/problem/10816

# Type 1. Dictionary
'''
import sys
input = sys.stdin.readline

_ = input()
num_cards = list(map(int, input().split()))
_ = input()
targets = list(map(int, input().split()))

how_many = {}

for i in num_cards:
    if i in how_many:
        how_many[i] += 1
    else:
        how_many[i] = 1

print(' '.join(str(how_many[j]) if j in how_many else '0' for j in targets))
'''

# Type 2. Collection

import sys
from collections import Counter
input = sys.stdin.readline



_ = input()
num_cards = list(map(int, input().split()))
_ = input()
targets = list(map(int, input().split()))

how_many = Counter(num_cards)

print(' '.join(f'{how_many[j]}' if j in how_many else '0' for j in targets))