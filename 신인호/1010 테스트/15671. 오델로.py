import sys
sys.stdin = open(f'{__file__.split(".py")[0]} input.txt', 'r')
input = sys.stdin.readline


# 상대편 돌의 색이 뭔지 알려줌
def another(color):
    if color == 'B':
        return 'W'
    else:
        return 'B'


def dfs(row, col, direction_num, color):
    # 범위 체크
    if not (1 <= row <= 6 and 1 <= col <= 6):
        return False

    # 상대편 돌이 계속 이어지는 경우
    if board[row][col] == color:
        y = row + dy[direction_num]
        x = col + dx[direction_num]
        # 똑같은 방향으로 계속 나아가며 색 검사
        turn_around = dfs(y, x, direction_num, color)
        # 이후의 결과가 뒤집는 거였으면, 색 바꾸기
        if turn_around:
            board[row][col] = another(color)
            # 이전 돌의 색도 바꾸기 위해, True 리턴
            return True
    # 이어지다가 내 돌을 만난 경우엔
    elif board[row][col] == another(color):
        # 이전까지 이어지던 상대편 돌들 바꾸라는 신호 전달
        return True
    # 아무것도 없는 공간인 경우엔, 이전 돌들 그대로 놔둠
    else:
        return False


# 상 하 좌 우 우상 우하 좌상 좌하
dy = (-1, 1, 0, 0, -1, 1, -1, 1)
dx = (0, 0, -1, 1, 1, 1, -1, -1)

# 게임판 초기 상태 (1부터 시작하기 위해 7칸을 씀)
board = [['.'] * 7 for _ in range(7)]
board[3][3] = board[4][4] = 'W'
board[3][4] = board[4][3] = 'B'

N = int(input())
for i in range(1, N + 1):
    # 돌 위치 입력받고, 순서에 맞는 색을 해당 위치에 기록
    row, col = map(int, input().split())
    color = 'B' if i % 2 else 'W'
    board[row][col] = color
    
    # 돌 주변 모든 방향에 대해
    for j in range(8):
        y = row + dy[j]
        x = col + dx[j]
        # 탐색
        dfs(y, x, j, another(color))

# 돌 개수 세기
black = 0
white = 0
for row in board:
    black += row.count('B')
    white += row.count('W')
winner = 'Black' if black > white else 'White'

print('\n'.join(''.join(row[1:]) for row in board[1:]))
print(winner)
