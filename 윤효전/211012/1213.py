import sys
input = sys.stdin.readline

import collections

def chk(t):
    c = ''
    for key, value in t:
        if value % 2 == 1 and c != '':
            return False
        elif value % 2 == 1:
            c = key
    return c


S = input().rstrip()

s = collections.Counter(S)
t = s.items()
t = sorted(t)
r = chk(t)
if r == False:
    print("I'm Sorry Hansoo")
else:
    a = ''
    for key, value in t:
        a += key*(value//2)
    print(a + r + a[::-1])