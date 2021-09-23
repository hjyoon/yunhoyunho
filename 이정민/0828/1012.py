dx = [-1,1,0,0]     #델타
dy = [0,0,-1,1]


def bfs(v, w):
    Q = []
    # enQ
    Q.append((v, w))
    visited[v][w] = 1

    while Q:
        (v, w) = Q.pop(0)
        # (v,w)의 인접한 정점중에 방문 안한 정점 (x,y)
        for i in range(4):
            x = v + dx[i]
            y = w + dy[i]
            if not x < 0 and not y < 0 and not x >= N and not y >= M:
                if arr[x][y] == 1 and visited[x][y] == 0:
                    visited[x][y] = visited[v][w] + 1
                    Q.append((x, y))
    return 0


T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]  # 방문

    for i in range(K):
        inputx, inputy = map(int, input().split())
        arr[inputy][inputx] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1

    print(cnt)
