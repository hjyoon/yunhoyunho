from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def count_diff(base, aux):
    diff = 0
    for row in range(H):
        for col in range(W):
            # 다르면 개수 증가
            if pictures[base][row][col] != pictures[aux][row][col]:
                diff += 1
                # 백트래킹: 최소보다 많으면 스킵
                if diff >= min_diff:
                    return diff
    return diff
        
    
# 가로, 세로
W = 7
H = 5

N = int(input())

# 그림 입력
pictures = []
for _ in range(N):
    picture = [list(input()) for _ in range(H)]
    pictures.append(picture)

# 가장 작은 경우의 그림 번호
min_diff = H * W
min_base, min_aux = 0, 0

# 기준을 한 칸씩 옮겨가면서, 
# 기준 다음에 있는 나머지 그림들과 비교
for base in range(N - 1):
    for aux in range(base + 1, N):

        diff = count_diff(base, aux)
        if diff < min_diff:
            min_diff = diff
            min_base = base
            min_aux = aux

print(min_base + 1, min_aux + 1)
