# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Mar 2 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 10871, BJ Online Judge
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split())
number = list(map(int, input().split()))
# list type, https://wikidocs.net/14
# list - input, https://art-coding3.tistory.com/6 https://dojang.io/mod/page/view.php?id=2286

for loop in range(n):
    if number[loop] < x:
        print(number[loop], end=' ')


# END 

