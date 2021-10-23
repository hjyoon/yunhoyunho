from sys import stdin
def bfs(x):
    head = 0
    tail = 1
    queue = [0] * 10001
    queue[0] = x
    visited[x] = 1

    while head!=tail:
        now = queue[head]
        head += 1

        for i in range(1, N+1):
            if arr[now][i] == 1:
                next = i

                if visited[next] != 0:
                    continue

                if visited.count(0) == 1:
                    return

                queue[tail] = next
                tail+=1
                visited[next]= visited[now] + 1
    return
T = int(stdin.readline())
for tc in range(1,T+1):
    airplane = []
    N, M = map(int, stdin.readline().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for i in range(M):
        a, b = map(int, stdin.readline().split())
        airplane.append((a,b))
        arr[a][b] = 1
        arr[b][a] = 1

    for i in range(len(airplane)):
        bfs(airplane[i][0])
    print(max(visited))


# T = int(stdin.readline())
# for tc in range(1,T+1):
#     N, M = map(int, stdin.readline().split())
#     for i in range(M):
#         a, b = map(int, stdin.readline().split())
#     print(N-1)