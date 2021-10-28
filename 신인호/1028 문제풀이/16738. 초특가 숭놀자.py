from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
* 구현 문제 
    <- 그리디 X, DP X, 탐색 X
    <- 매 단계마다 다양한 상황이 주어지기 때문

0. 큰 수 -> L, R 경계값만 필요

1. 추가 
    -> 항상 좌측 빈 방부터
    -> 항상 좌측부터 찾아야 함
    -> 방 시작 번호 기준, 오름차순 '정렬' 필요 
    -> 정렬 (혹은 연결 리스트)

2. 삭제
    -> 시간 순으로 찾음
    -> 추가할 때마다 위치 변해서
    위치 인덱스 연동은 불가
    -> 그냥 '순회' 필요
"""

N, Q = map(int, input().split())
rooms = []
room_count = 1

for _ in range(Q):
    task, x, y = input().split()
    if task == 'new':
        people = int(x)
        needed = int(y)
        next_left = prev_right = 0

        # 현재 방 끝 번호 ~ 다음 방 시작 번호 간격이 
        # 요구되는 방의 크기보다 크면 됨.
        for room in rooms:
            next_left = room[0]
            if next_left - prev_right > needed:
                break
            prev_right = room[1]
        
        # 끝까지 돌았는데도 요구를 충족 못 시키면 넘김.
        if N - prev_right < needed:
            print('REJECTED')
            continue

        # 현재 방 다음 ~ 필요한 만큼. 다른 값들도 추가
        rooms.append([prev_right + 1, prev_right + needed, people, room_count])
        # 방 시작 순서로 정렬!!!
        rooms.sort()
        room_count += 1

        print(prev_right + 1, prev_right + needed)
    
    elif task == 'in':
        room_num = int(x)
        people = int(y)

        # 맞는 방 번호 찾아서 사람 추가
        for room in rooms:
            if room[3] == room_num:
                room[2] += people
                break
    
    elif task == 'out':
        room_num = int(x)
        people = int(y)
        isEmpty = False

        # 맞는 방 번호 찾아서 사람 빼기
        for i in range(len(rooms)):
            if rooms[i][3] == room_num:
                rooms[i][2] -= people
                # 0이 되면 방 비워야 함
                if rooms[i][2] == 0:
                    isEmpty = True
                break

        # 0이었던 경우 방 비우기
        if isEmpty:
            left, right, people, room_num  = rooms.pop(i)
            print(f'CLEAN {left} {right}')
