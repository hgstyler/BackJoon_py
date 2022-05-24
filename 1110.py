# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by Henry, Mar 3 2022
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 1110, BJ Online Judge
# https://www.acmicpc.net/problem/1110

N_origin = int(input())
N = int(N_origin)
counter = int(0)

while True:
    N = (N % 10) * 10 + (N // 10 + N % 10) % 10 # keep in mind '//' operator, '/' is not integer result
    counter += 1 # i++ in Python, https://ondemand.tistory.com/255
    if N != N_origin: continue
    break
# do-while type statement in Python, https://woogyun.tistory.com/519

print(counter)

# END

