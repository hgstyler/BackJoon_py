# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 4153, BJ Online Judge
# https://www.acmicpc.net/problem/4153

import sys
input = sys.stdin.readline

tmp1 = int(1); tmp2 = int(1); tmp3 = int(1)
tri_lst = []
tri_res = []

while tmp1 != 0 and tmp2 != 0 and tmp3 != 0:
    tmp1, tmp2, tmp3 = map(int, input().split())

    tri_lst.append(tmp1); tri_lst.append(tmp2); tri_lst.append(tmp3)
    tri_lst.sort()

    tri_condition = bool(tri_lst[0] ** 2 + tri_lst[1] ** 2 == tri_lst[2] ** 2)

    if tmp1 != 0 and tmp2 != 0 and tmp3 != 0:
        if tri_condition:
            tri_res.append("right")
        else:
            tri_res.append("wrong")

    tri_lst.clear()

for i in tri_res:
    print(i)

# END
