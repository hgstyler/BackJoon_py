# ############################
# BJ Online Judge Project
# by hgstyler based on Python
# ############################

# Question 10872, BJ Online Judge
# https://www.acmicpc.net/problem/10872

def fact(n, s):
    if n > 1:
        s[0] *= n
        fact(n-1, s)
    else:
        return
    
n = int(input())
product_sum = [1]

fact(n, product_sum)

print(product_sum[0])

# END