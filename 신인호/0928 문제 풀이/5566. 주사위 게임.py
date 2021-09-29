from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
두 번째 지시 때는 이동 X
N칸 이상 => 도착
무조건 도착 가능
"""

N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]

cur_pos = 0
for i in range(M):
    # 주사위 수만큼 이동
    next_move = dice[i]
    cur_pos += next_move
    # 도착 지점 넘기면 주사위 수 출력
    if cur_pos >= N - 1:
        print(i + 1)
        break

    # 보드 현재 위치의 지시만큼 이동
    next_move = board[cur_pos]
    cur_pos += next_move
    # 도착 지점 넘기면 주사위 수 출력
    if cur_pos >= N - 1:
        print(i + 1)
        break
