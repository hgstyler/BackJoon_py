# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 1427, BJ Online Judge
# https://www.acmicpc.net/problem/1427

import sys
input = sys.stdin.readline

print(''.join(sorted(input().rstrip(), reverse=True)))

# about sorting https://docs.python.org/ko/3/howto/sorting.html
# reverse str https://velog.io/@joygoround/test-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4%EB%A6%BC%EC%B0%A8%EC%88%9C%EC%9C%BC%EB%A1%9C-%EB%B0%B0%EC%B9%98%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# convert list to str https://codechacha.com/ko/python-convert-list-to-string/
# convert list to tuple, vice versa https://waytods.tistory.com/19