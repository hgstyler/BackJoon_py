# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 10815, BJ Online Judge
# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

def binary_search(lst, num):
    low = 0
    high = len(lst) - 1

    while (low <= high):
        mid = (low + high) // 2

        if lst[mid] == num:
            return 1
        elif lst[mid] > num:
            high = mid - 1
        else:
            low = mid + 1

    return 0

n = int(input())
numbers = [int(x) for x in input().split()]

numbers.sort()

m = int(input())
targets = [int(x) for x in input().split()]

for tmp in targets:
    print(binary_search(numbers, tmp), end=' ')

# TMI. bisect.bisect method
'''
import bisect

print(f'\n\nnumbers: {numbers}\ntargets: {targets}\nbisect.bisect_left : ', end='')
for tmp in targets:
    print(bisect.bisect_left(numbers, tmp), end=' ')
print()

print('bisect.bisect      : ', end='')
for tmp in targets:
    print(bisect.bisect(numbers, tmp), end=' ')
print()

print('bisect.bisect_right: ', end='')
for tmp in targets:
    print(bisect.bisect_right(numbers, tmp), end=' ')
print()
'''