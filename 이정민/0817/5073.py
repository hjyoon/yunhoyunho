

#리스트 만들어서 max값 따로빼서 나머지랑 비교
while True:
    try:
        triangle = [list(map(int, input().split()))]

        for i in range(len(triangle)):
            tri = []
            for j in range(3):
                tri.append(triangle[i][j])
            if triangle[i][0] == 0 and triangle[i][1] == 0 and triangle[i][2] == 0:
                break
            if max(tri) < (sum(tri) - max(tri)):
                if triangle[i][0] == triangle[i][1] and triangle[i][1] == triangle[i][2] and triangle[i][2] == \
                        triangle[i][0]:
                    print('Equilateral')
                    continue
                if triangle[i][0] != triangle[i][1] and triangle[i][1] != triangle[i][2] and triangle[i][2] != \
                        triangle[i][0]:
                    print('Scalene')
                    continue
                else:
                    print('Isosceles')
                    continue
            else:
                print('Invalid')
    except:
        break