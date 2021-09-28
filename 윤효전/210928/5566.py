import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [None] + [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]

pos = 1
i = 0
cnt = 0
bonus = False
while pos < N:
    if board[pos] == 0 or not bonus:
        pos += dice[i]
        i += 1
        bonus = True
    else:
        if bonus:
            pos += board[pos]
            bonus = False
        else:
            pass

print(i)
