# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 11729, BJ Online Judge
# https://www.acmicpc.net/problem/11729

def moving(f, t, vv, kk):
    kk[0] += 1
    vv.append(f+' '+t)
    return

def hanoi(n, f, t, v, vv, kk):
    if n == 1:
        moving(f, t, vv, kk)
    else:
        hanoi(n-1, f, v, t, vv, kk)
        moving(f, t, vv, kk)
        hanoi(n-1, v, t, f, vv, kk)
    return

num = int(input())
k = [0]
history = []

hanoi(num, '1', '3', '2', history, k)

print(k[0])
for i in history:
    print(i)

# END