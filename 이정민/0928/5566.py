N, M = map(int,input().split())

boardgame = []
for i in range(N):
    boardgame.append(int(input()))

print(boardgame)

dice = []
for j in range(M):
    dice.append(int(input()))
print(dice)

now = 0 # 현재 위치한 칸
cnt = 0 # 주사위를 던진 횟수
for k in dice:
    now += k
    cnt += 1
    if now >= N:
        break
    now += boardgame[now]
    if now >= N:
        break

print(cnt)