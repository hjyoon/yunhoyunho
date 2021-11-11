from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

from collections import deque

"""
방문하기 전에 방문 체크부터
방문 체크 하자마자 바로 방문

FIXME: 방문 체크 이전에 방문부터 하면,
queue 같은 경우엔, 중복해서 방문하게 됨
(<- 큐에 들어갈 때는 아직 방문하지 않았을 수도 있으므로)
"""

def dfs(s):
    if not used[s]:
        used[s] = True
        print(s, end=' ')

        for e in adj_list[s]:
            dfs(e)


def bfs(s):
    queue = deque()
    queue.append(s)

    while queue:
        s = queue.popleft()
        if not used[s]:
            used[s] = True
            print(s, end=' ')
            for e in adj_list[s]:
                queue.append(e)


N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

for s in range(1, N + 1):
    adj_list[s].sort()

used = [False] * (N + 1)
dfs(V)
print()

used = [False] * (N + 1)
bfs(V)
