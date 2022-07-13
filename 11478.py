# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11478, BJ Online Judge
# https://www.acmicpc.net/problem/11478

import sys
input = sys.stdin.readline

s = input().rstrip()
string_set = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j+1]:
            string_set.add("".join(s[i:j+1])) # slicing https://twpower.github.io/119-python-list-slicing-examples https://dojang.io/mod/page/view.php?id=2208

print(len(string_set))