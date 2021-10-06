import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def chk(S, N, b):
    left, right = b, b
    while True:
        if left-1 < 1 or right+1 > N:
            break
        if S[left-1] != S[right+1]:
            break
        left -= 1
        right += 1
    return left, right


N = int(input())
S = [None] + list(map(int, input().split()))
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:  # 남
        for i in range(b, N+1, b):
            S[i] = 1 - S[i]
    else:  # 여
        left, right = chk(S, N, b)
        for i in range(left, right+1):
            S[i] = 1 - S[i]

for i in range(1, len(S), 20):
    print(*S[i:i+20])
