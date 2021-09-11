"""
가로 방향 판자가 있으면 무조건 가로 방향만 조사하면 된다.
그래서 쭉 조사하다가, 세로 방향이 나오면 그 전까지가 하나의 판자다.

여기서 바로 다음 세로 방향의 판자로 넘어가서 찾기 시작하면 복잡해진다.
왜냐하면 오른쪽에 아직 조사하지 못한 판자들이 남아있는데,
계속해서 가로, 세로를 왔다갔다 하면 어디서부터 분기되었는지 알기 힘들다.

따라서 심플하게, 그냥 visited 행렬을 이용한다.
1. 일단 한쪽 방향에 대한 검사와 동시에 visited를 체크한다.
2. 만약 끝까지 가면 거기서 멈춘다.
3. 다시 시작점으로 돌아와 visited를 체크해나간다.
4. 방문했던 점은 넘어가면 된다.
"""


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
board_num = 0

for row in range(N):
    for col in range(M):
        # 체크한 적 없는 바닥
        if not visited[row][col]:

            # 가로 방향 판자에 대해
            if arr[row][col] == '-':
                # 현재 위치부터 끝까지
                for x in range(col, M):
                    # 열만 증가시키며 이어지는지 체크
                    if arr[row][x] == '-':
                        # 이어지면 방문 체크
                        visited[row][x] = True
                    else:
                        # 이어지지 않으면 판자 하나 완성
                        board_num += 1
                        break
                # 행의 끝까지 무사히 이어지는 경우도 있음
                # = break로 나오지 않은 경우
                else:
                    board_num += 1

            # 세로 방향 판자에 대해서 위와 비슷하게 구현
            else:
                for y in range(row, N):
                    if arr[y][col] == '|':
                        visited[y][col] = True
                    else:
                        board_num += 1
                        break
                else:
                    board_num += 1

print(board_num)