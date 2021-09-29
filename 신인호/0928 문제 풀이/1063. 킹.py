from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


movements = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1)
}

# 행 위치를 숫자 <=> 영문자로 바꾸는 함수
row_alpha = lambda i: chr(i + ord('A') - 1)
row_num = lambda a: ord(a) - ord('A') + 1

# 입력 받고 전부 숫자로 바꾸기
king, stone, N = input().split()
king_x = row_num(king[0])
king_y = int(king[1])
stone_x = row_num(stone[0])
stone_y = int(stone[1])
N = int(N)

for _ in range(N):
    # 이번 입력
    move = input().rstrip()
    
    # 입력 길이에 따라 이동 횟수 구하기
    dx = dy = 0
    for m in move:
        dx += movements[m][0]
        dy += movements[m][1]
    
    x = king_x + dx
    y = king_y + dy
    # 킹이 이동 가능한 범위인지
    if 1 <= x <= 8 and 1 <= y <= 8:
        # 이동 후 위치가 돌이랑 겹치는지
        if x == stone_x and y == stone_y:
            # 돌이 이동 가능한 범위인지
            if 1 <= stone_x + dx <= 8 and 1 <= stone_y + dy <= 8: 
                # 돌 이동
                stone_x += dx
                stone_y += dy
            # NOTE: 돌을 밀 수 없으면 킹도 이동 불가
            else:
                continue
        # 킹 이동
        king_x += dx
        king_y += dy
    # print(king_x, king_y, stone_x, stone_y)

king_x = row_alpha(king_x)
stone_x = row_alpha(stone_x)
print(f'{king_x}{king_y}')
print(f'{stone_x}{stone_y}')
