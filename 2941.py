# * ** * ** *** ** * ** *
# BJ Online Judge Project
# by hgstyler based on Python
# * ** * ** *** ** * ** *

# Question 2941, BJ Online Judge
# https://www.acmicpc.net/problem/2941

def dzeq(w, l):
    chk = 0
    for cnt in range(0,l-2):
        if w[cnt] == 'd':
            if w[cnt+1] == 'z':
                if w[cnt+2] == '=':
                    chk += 1

    return chk

def lj(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 'l':
            if w[cnt+1] == 'j':
                chk += 1

    return chk

def nj(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 'n':
            if w[cnt+1] == 'j':
                chk += 1

    return chk

def ceq(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 'c':
            if w[cnt+1] == '=':
                chk += 1

    return chk

def chphen(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 'c':
            if w[cnt+1] == '-':
                chk += 1

    return chk

def dhphen(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 'd':
            if w[cnt+1] == '-':
                chk += 1

    return chk

def seq(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 's':
            if w[cnt+1] == '=':
                chk += 1

    return chk

def zeq(w, l):
    chk = 0
    for cnt in range(0,l-1):
        if w[cnt] == 'z':
            if w[cnt+1] == '=':
                chk += 1

    return chk

words = input()
words_cnt = 0

words_cnt += dzeq(words, len(words))
words = words.replace('dz=','0')

words_cnt += ceq(words, len(words))
words = words.replace('c=','0')

words_cnt += chphen(words, len(words))
words = words.replace('c-','0')

words_cnt += dhphen(words, len(words))
words = words.replace('d-','0')

words_cnt += seq(words, len(words))
words = words.replace('s=','0')

words_cnt += zeq(words, len(words))
words = words.replace('z=','0')

words_cnt += lj(words, len(words))
words = words.replace('lj','0')

words_cnt += nj(words,len(words))
words = words.replace('nj','0')

words = words.replace('0','')
words_cnt += len(words)

print(words_cnt)

# END
