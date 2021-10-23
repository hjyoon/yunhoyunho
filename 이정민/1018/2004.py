import sys
sys.setrecursionlimit(10**9)
# # nCm
n, m = map(int,input().split())
# factnum = 1
#
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#
# if n == m :
#     print(0)
#
# elif n==0 or m==0:
#     print(0)

# else:
import math
# calc = []
# calc.append(factorial(n))
# calc.append(factorial(m))
# calc.append(factorial(n-m))
a = factorial(n)
b = factorial(m)
c = factorial(n-m)

ans = a//(b*c)
# number = list(ans)

cnt = 0

while (ans%10) == 0:
    ans = ans // 10
    cnt+=1

# for i in range(len(number)-1,-1,-1):
#     if number[i] != '0':
#         break
#     if number[i] == '0':
#         cnt+=1

print(cnt)