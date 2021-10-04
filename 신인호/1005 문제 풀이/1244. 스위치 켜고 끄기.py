from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
남자 -> 배수
여자 -> 대칭
단, 둘 다 스위치 범위 내에 속해야 함
"""

switch_num = int(input())
switches = list(map(int, input().split()))
student_num = int(input())
students = [list(map(int, input().split())) for _ in range(student_num)]

for student in students:
    given_num = student[1]

    # 남자(1)인 경우
    if student[0] == 1:
        # 받은 숫자부터 끝까지, 받은 숫자만큼의 간격으로
        for i in range(given_num - 1, switch_num, given_num):
            # XOR 연산을 통해 0과 1을 토글
            switches[i] ^= 1
    # 여자인 경우
    else:
        # 받은 숫자만큼 주위를 둘러봄
        for i in range(given_num):
            # 인덱스 범위 체크
            # FIXME: 시작이 1번이므로, 항상 -1을 해줘야 함
            if 0 <= given_num - 1 - i and given_num - 1 + i < switch_num:
                # 양쪽이 대칭인 경우
                if switches[given_num - 1 - i] == switches[given_num - 1 + i]:
                    # 양쪽 스위치 상태 변경
                    switches[given_num - 1 - i] ^= 1
                    switches[given_num - 1 + i] = switches[given_num - 1 - i]
                # 대칭이 아닌 경우 거기서 중지
                else:
                    break
            # 인덱스 벗어나도 중지
            else:
                break

# FIXME: 한 줄에 20개씩 출력해야 함
for i in range(switch_num):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
