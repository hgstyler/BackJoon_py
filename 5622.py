# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 5622, BJ Online Judge
# https://www.acmicpc.net/problem/5622

dial_sec = [ 3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10 ]

dial = str(input())
sum = 0

for cnt in range(len(dial)):
    sum += dial_sec[ord(dial[cnt]) - 65] # ord vs. chr https://blockdmask.tistory.com/544
    
print(sum)