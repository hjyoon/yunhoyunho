from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
모든 아기 상어들과의 거리 계산 필요
=> queue에 아기 상어 위치 전부 집어넣고,
=> BFS 방식으로 최소 거리 갱신하기

이때, 자기보다 작은 수가 나오면 멈추기
(<- 이미 다른 상어로부터 더 짧은 거리가 있으므로)
"""

H, W = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

# 거리 배열 필요
distances = [[W + H] * W for _ in range(H)]
max_distance = 0

# 큐 준비
size = 2 * H * 2 * W
queue = [0] * size
front = -1
rear = -1

# 큐에 초기 위치 집어넣기
for row in range(H):
    for col in range(W):
        if arr[row][col]:
            rear = (rear + 1) % size
            queue[rear] = (row, col, 0)
            # 시작점은 거리를 0으로 초기화
            distances[row][col] = 0

# 8 방향 탐색: 상 하 좌 우, 좌상 좌하 우상 우하
dy = (-1, 1, 0, 0, -1, 1, -1, 1)
dx = (0, 0, -1, 1, -1, -1, 1, 1)

# BFS로 안전 거리 갱신
while front != rear:
    front = (front + 1) % size
    row, col, cur_path = queue[front]

    for i in range(8):
        y = row + dy[i]
        x = col + dx[i]

        # 범위 체크
        if not (0 <= x < W and 0 <= y < H):
            continue
        # 더 길면 pass
        if distances[y][x] <= cur_path + 1:
            continue
        # 더 짧은 거리로 갱신
        distances[y][x] = cur_path + 1
        
        # 큐에 새 후보 넣기
        rear = (rear + 1) % size
        queue[rear] = (y, x, cur_path + 1)

        # 답 갱신
        if max_distance < cur_path + 1:
            max_distance = cur_path + 1

print(max_distance)
