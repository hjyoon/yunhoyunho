import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = [None] + [int(input()) for _ in range(N)]

cnt_max = 0
ans = 0
for i in range(1, N+1):
    visit = [None] + [0]*N
    cur = i
    cnt = 0
    while True:
        if visit[cur] == 0:
            visit[cur] = 1
            cur = S[cur]
            cnt += 1
        else:
            break
    if cnt_max < cnt:
        cnt_max = cnt
        ans = i

print(ans)
