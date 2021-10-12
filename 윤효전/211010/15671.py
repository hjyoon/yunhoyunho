import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

BOARD_H, BOARD_W = 6, 6


# 어떤 컬러가 이겼는지 리턴
def what_color_win(l):
    white, black = 0, 0
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            if l[i][j] == 'W':
                white += 1
            elif l[i][j] == 'B':
                black += 1
            else:
                pass
    if white > black:
        return 'White'
    else:
        return 'Black'


# 게임판에서 특정 좌표들을 해당 컬러로 모두 바꾼다
def reverse_color(l, pos_l, color):
    for y, x in pos_l:
        l[y][x] = color


# 게임판에서 어떤 좌표들이 바뀔 수 있는지 모두 찾아서 리턴
def get_pos_need_to_change(y, x, l):
    ret = []
    d_pos = (
        (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    )
    base_color = l[y][x]
    for dy, dx in d_pos:
        ty, tx = y, x
        tmp_pos_l = []
        while True:
            ty += dy
            tx += dx
            if ty < 0 or ty >= BOARD_H or tx < 0 or tx >= BOARD_W:
                break
            if l[ty][tx] == base_color:
                ret.extend(tmp_pos_l)
                break
            elif l[ty][tx] != '.':
                tmp_pos_l.append((ty, tx))
            else:
                break
    return ret


ans = None
N = int(input())

# 초기 게임판
board = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', 'W', 'B', '.', '.'],
    ['.', '.', 'B', 'W', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

# 흑 선 (턴을 넘겨야 하는 경우 X, 항상 올바른 입력 보장)
for i in range(N):
    r, c = map(lambda x: int(x)-1, input().split())
    color = ['B', 'W'][i % 2]
    board[r][c] = color
    pos_l = get_pos_need_to_change(r, c, board)
    reverse_color(board, pos_l, color)

# 최종 게임판 출력
for i in range(len(board)):
    print(*board[i], sep='')

# 승자 출력 (비기는 경우 X)
ans = what_color_win(board)
print(ans)