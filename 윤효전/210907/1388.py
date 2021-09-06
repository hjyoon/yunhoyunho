from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
visit = [[0]*C for _ in range(R)]


def dfs(y, x, pre):
    if y < 0 or x < 0 or y >= R or x >= C:
        return

    if visit[y][x] == 1:
        return

    if pre != board[y][x]:
        return

    visit[y][x] = 1
    if board[y][x] == '-':
        dfs(y, x+1, '-')
    else:
        dfs(y+1, x, '|')


ans = 0
for i in range(R):
    for j in range(C):
        if visit[i][j] == 0:
            dfs(i, j, board[i][j])
            ans += 1

print(ans)
