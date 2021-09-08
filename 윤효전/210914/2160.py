from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    tmp = [input().rstrip() for _ in range(5)]
    S.append(tmp)


def custom_cmp(a, b):
    ret = 0
    for i in range(5):
        for j in range(7):
            if S[a][i][j] != S[b][i][j]:
                ret += 1
    return (ret, a, b)


ans = (100, -1, -1)
for i in range(N):
    for j in range(i+1, N):
        tmp = custom_cmp(i, j)
        if tmp[0] < ans[0]:
            ans = tmp

print(ans[1]+1, ans[2]+1)
