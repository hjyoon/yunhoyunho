'''

if 4번째가 1이면:
앞의 3개 번호들 -> 정상처리

나머지 케이스들 중에 정상인 애들이 있으면 걔들은 뻄

뺐는데 하나만 남은 케이스들 -> 하나 남은 애는 고장임
두개 남은 애들은 보류

그 하나를 또 다른 케이스들에서 빼줌

두개 남았던 애들 중에 이제 고장난애 뺐는데 고장인 애들은 알수없음으로 처리

'''


a, b, c = map(int, input().split())
N = int(input())

A = list(range(1,a+1))
B = list(range(a+1,a+b+1))
C = list(range(a+b+1,a+b+c+1))

parts = []
for n in range(N):
    i, j, k, r = map(int,input().split())
    parts.append([i,j,k,r])
# [[2, 4, 5, 0], [2, 3, 6, 0], [1, 4, 5, 0], [2, 3, 5, 1]]

operate = []
notoperate = []
dontknow = []
for m in range(len(parts)):
    if parts[m][3] == 1:
        operate.append(parts[m][0])
        operate.append(parts[m][1])
        operate.append(parts[m][2])
#operate = [2,3,5]

for m in range(len(parts)):
    for n in range(3):
        if parts[m][3] == 0:
            if parts[m][n] in operate:
                parts[m][n] = -1
# [[-1, 4, -1, 0], [-1, -1, 6, 0], [1, 4, -1, 0], [2, 3, 5, 1]]

for m in range(len(parts)):
    while -1 in parts[m]:
        parts[m].remove(-1)
    # [[ 4, 0], [ 6, 0], [1, 0] [1,1,1,0]]
    if len(parts[m]) == 2: #알수없는 부품이 포함이 안된 확실히 고장난 애들만 있는 경우
        notoperate.append(parts[m][0])
    # notoperate = [4,6]
for m in range(len(parts)):
    if parts[m][-1] == 0:
        if len(parts[m]) >= 3:
            for n in notoperate:
                if n in parts[m]:
                    parts[m].remove(n)
            dontknow.append(parts[m][0])
 #dontknow = [1]

for i in A:
    if i in operate:
        print(1)
    elif i in notoperate:
        print(0)
    else:
        print(2)

for i in B:
    if i in operate:
        print(1)
    elif i in notoperate:
        print(0)
    else:
        print(2)

for i in C:
    if i in operate:
        print(1)
    elif i in notoperate:
        print(0)
    else:
        print(2)















