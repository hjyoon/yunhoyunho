
arr = [list(input().split()) for _ in range(8)]



cnt = 0
for i in range(8):
    if i%2:
        for j in range(1):
            for k in range(8):
                if k % 2:
                    if arr[i][j][k] == 'F':
                        cnt += 1
    if i%2 ==0:
        for j in range(1):
            for k in range(8):
                if k % 2 == 0:
                    if arr[i][j][k] == 'F':
                        cnt += 1
print(cnt)



# 홀수가 하얀칸임