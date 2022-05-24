# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler
# Dev. Language: Python
# * ** * ** *** ** * ** *

# Question 4344, BJ Online Judge
# https://www.acmicpc.net/problem/4344

C = int(input())

for cnt in range(C):
    class_info = list(map(int,input().split()))
    sum = 0
    over_avg_students = 0
    for cnt2 in range(1, class_info[0]+1):
        sum = sum + class_info[cnt2]
    avg_class = sum / class_info[0]
    for cnt2 in range(1, class_info[0]+1):
        if class_info[cnt2] > avg_class:
            over_avg_students = over_avg_students + 1
    
    # res = round(over_avg_students/class_info[0]*100)
    res = over_avg_students/class_info[0]*100
    print(f'{res:.3f}%')

# END
