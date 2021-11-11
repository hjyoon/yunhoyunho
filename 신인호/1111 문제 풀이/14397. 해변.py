from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
해변 = 땅에서 물과 맞닿은 곳
해변 길이 = 땅에서 물과 맞닿은 칸의 개수
예) 땅 1칸을 물 6칸이 둘러싸고 있으면 => 해변 길이는 6

=> 땅이 나올 때마다 주변 6 방향 둘러보면 됨

* NOTE: 6방향 위치는 줄마다 다름.
홀수 번째:
좌상, 상
좌, 우
좌하, 하

짝수 번째:
상, 우상,
좌, 우,
하, 우하

* DFS나 BFS는 아님.
딱 한 칸씩만 둘러보면 되니까.
"""

HEIGHT, WIDTH = map(int, input().split())
MAP = [input() for _ in range(HEIGHT)]
length = 0

dy = (-1, 1, 0, 0, -1, 1)
# 홀수 줄: 상, 하, 좌, 우, 좌상, 좌하
dx_odd = (0, 0, -1, 1, -1, -1)
# 짝수 줄: 상, 하, 좌, 우, 우상, 우하
dx_even = (0, 0, -1, 1, 1, 1)


for row in range(HEIGHT):
    for col in range(WIDTH):
        # 땅인 경우
        if MAP[row][col] == '#':
            for i in range(6):
                y = row + dy[i]
                # 홀수 번째 줄 방향
                if row % 2 == 0:
                    x = col + dx_odd[i]
                # 짝수 번째 줄 방향
                else:
                    x = col + dx_even[i]

                # 범위 체크
                if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
                    continue
                # 맞닿은 곳이 물이면 해변 길이 1 증가
                if MAP[y][x] == '.':
                    length += 1

print(length)
