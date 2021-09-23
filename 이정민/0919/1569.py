N = int(input())
arr = [[0]*3000 for _ in range(3000)]

asd = []
# --------------------------------------------
for i in range(N):
    x, y = map(int, input().split())
    asd.append([x,y])

# (part 1) x, y가 음수이면 가장 음수값이 큰 수의 절대값을 더해준다.
# x값
min = 0
for i in range(N):
    if asd[i][0] < 0:
        if asd[i][0] < min:
            min = asd[i][0]
for i in range(N):
    asd[i][0] += abs(min)

#y값
min = 0
for i in range(N):
    if asd[i][1] < 0:
        if asd[i][1] < min:
            min = asd[i][1]
for i in range(N):
    asd[i][1] += abs(min)

print(asd)
# ------------------------------------------------

# (part 2) 각각 점에 해당하는 좌표를 arr에서 1로 바꿔줌
for i in range(N):
    arr[asd[i][0]][asd[i][1]] = 1

maxX = -987654321
minX = 987654321

maxY = -987654321
minY = 987654321

# 각 좌표의 최대, 최소값을 구한다
for i in range(N):
    if maxX < asd[i][0]:
        maxX = asd[i][0]
    if minX > asd[i][0]:
        minX = asd[i][0]
    if maxY < asd[i][1]:
        maxY = asd[i][1]
    if minY > asd[i][1]:
        minY = asd[i][1]


# 가장 좌,우측의 X값에 해당하는 Y값을 모조리 0으로 만들기
for i in range(minY,maxY+1):
    arr[minX][i] = 0
    arr[maxX][i] = 0

# 가장 위, 아래에 있는 Y값에 해당하는 X값을 모조리 0으로 만들기
for i in range(minX,maxX+1):
    arr[i][minY] = 0
    arr[i][maxY] = 0


#1.만약 maxX-minX 와 maxY-minY 값이 다르면(정사각형이 아니면) fail
if minY == maxY or minX == maxX:
    print(max(maxX - minX, maxY - minY))
else:
    if (maxX-minX) == (maxY-minY):
        flag = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == 1:
                    print(-1)
                    flag = 1
                    break
            if flag == 1:
                break

        if flag == 0:
            print(max(maxX - minX, maxY - minY))
    else:
        print(-1)
#2.만약 arr에 1이 남아있으면 fail

# flag = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i][j] == 1:
#             print(-1)
#             flag = 1
#             break
#
# if flag == 0:
#     print(max(maxX-minX, maxY-minY))










