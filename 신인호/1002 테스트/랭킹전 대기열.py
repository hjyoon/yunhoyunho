"""
<구조>
방이 만들어진 '순서대로' 출력 => '큐'?...
NOTE: 나중 방이 먼저 꽉 차서 먼저 실행될 수도 있음 
=> 그냥 리스트로 풀어야 함

<조건>
무조건 못 넣는 경우
1. 방이 꽉 찬 경우

무조건 넣는 경우
1. 방이 빈 경우
2. 이전 방들에 넣을 수 없던 경우 
    <- 이전 방 순회 필요
    => 나중에 배치

판별 필요
1. 기준 레벨 +- 10 이내

<흐름>
무조건 못 넣는 경우 -> 판별 -> 무조건 넣는 경우
"""

player_num, player_max = map(int, input().split())
players = [input().split() for _ in range(player_num)]

rooms = [0] * 300
rooms[0] = [players[0]]
room_num = 1

for x in range(1, player_num):
    for y in range(room_num):
        # 방이 꽉 차지 않았다면
        if len(rooms[y]) != player_max:
            # 레벨 비교해서, 조건 만족 시에만 넣기
            standard_level = int(rooms[y][0][0])
            newcomer_level = int(players[x][0])
            if abs(standard_level - newcomer_level) <= 10:
                rooms[y].append(players[x])
                break
    # 조건에 맞는 방이 없던 경우, 새 방에 넣기
    else:
        rooms[room_num] = [players[x]]
        room_num += 1

# 방 순서대로 출력
for x in range(room_num):
    if len(rooms[x]) == player_max:
        print('Started!')
    else:
        print('Waiting!')

    # 닉네임 순으로 정렬해서 출력
    rooms[x].sort(key=lambda x: x[1])
    for player in rooms[x]:
        print(*player)
