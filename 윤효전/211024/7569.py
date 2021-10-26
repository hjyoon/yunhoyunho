import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(visit, start):
    global H, N, M
    ret = 0
    dz = (0, 0, 0, 0, 1, -1)
    dy = (-1, 0, 1, 0, 0, 0)
    dx = (0, 1, 0, -1, 0, 0)
    dq = deque(start)
    while dq:
        z, y, x, cnt = dq.popleft()
        if z < 0 or z >= H or y < 0 or y >= N or x < 0 or x >= M:
            continue
        if visit[z][y][x] == 1:
            continue
        if S[z][y][x] == -1:
            continue
        ret = max(ret, cnt)
        visit[z][y][x] = 1
        for i in range(6):
            dq.append((z+dz[i], y+dy[i], x+dx[i], cnt+1))
    return ret


M, N, H = map(int, input().split())
S = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0]*M for _ in range(N)] for _ in range(H)]

start = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if S[i][j][k] == 1:
                start.append((i, j, k, 0))

ans = bfs(visit, start)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if S[i][j][k] == 0 and visit[i][j][k] == 0:
                ans = -1


print(ans)
