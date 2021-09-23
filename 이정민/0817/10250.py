T = int(input())
for tc in range(1,T+1):
    H, W, N = map(int,input().split())
    hotel = [[0]*H for _ in range(W)]

    for i in range(1,W+1):
        for j in range(1,H+1):
            hotel[i-1][j-1] = (100 * j) + i

    a = N//H # 만약 20이면  b는 2이므로 2층, a는 3이므로 i= 3 즉 hotel[a][b-1]
    b = N%H # 층 정하기
    if b>=1:
        print(hotel[a][b-1])
    else:
        print(hotel[a-1][b-1])
    # print(hotel)


    # 4
    # 10 10 10   1001
    # 10 10 11    102 a는 1, b는 1-1 = 0
    # 1 1 1         1
    # 99 99 9801    9999  a는 99, b는 0  즉 98, -1