N = int(input())
A = []
B = []
C = []
# three = [A.count(3), B.count(3), C.count(3)]
# two = [A.count(2), B.count(2), C.count(2)]
for i in range(N):
    a, b, c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
sums = [[sum(A), A.count(3), A.count(2), 1],
        [sum(B), B.count(3), B.count(2), 2],
        [sum(C), C.count(3), C.count(2), 3]]

asd = sorted(sums, key = lambda x : (-x[0], -x[1], -x[2]))

# 최고점수 셋 동일
if asd[0][0] == asd[1][0] == asd[2][0]:
    # 3점 셋 동일하면
    if asd[0][1] == asd[1][1] == asd[2][1]:
        # 2점 가장 많은사람 출력, else는 나머지 다 후보없음
        if asd[0][2] > asd[1][2]:
            print(asd[0][3], asd[0][0])
        else:
            print(0, asd[0][0])

    # 3점이 동일한게 2개
    if asd[0][1] == asd[1][1] != asd[2][1]:
        if asd[0][2] > asd[1][2]:
            print(asd[0][3], asd[0][0])
        else:
            print(0, asd[0][0])

    # 3점 제일 큰거 하나있을때
    if asd[0][1] > asd[0][2]:
        print(asd[0][3], asd[0][0])

# 최고점수 두명
    # idx값이 적을수록 3점이 더 많으므로
if asd[0][0] == asd[1][0] != asd[2][0]:
    if asd[0][1] > asd[1][1]:
        print(asd[0][3], asd[0][0])

    # 3점도 같은데 2점까지 같으면 후보 없음
    elif asd[0][1] == asd[1][1]:
        if asd[0][2] > asd[1][2]:
            print(asd[0][3], asd[0][0])
        else:
            print(0, asd[0][0])

# 최고점수 한명
if asd[0][0] != asd[1][0]:
    print(asd[0][3], asd[0][0])




