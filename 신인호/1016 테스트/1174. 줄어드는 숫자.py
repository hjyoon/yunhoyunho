from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
전략: 개선된 완전탐색
방식: 1씩 늘려가되, 
+ 매번 옆자리와 비교하여 옆자리보다 작은지 확인하고, 크면 바로 넘김
+ 자릿수가 늘어날 땐, 가능한 최소의 줄어드는 숫자부터 시작해서 또 넘김
"""

# T = int(input())
# for test_case in range(1, T + 1):
N = int(input())

if N > 1023:
    print(-1)
    exit()

# 자릿수만큼의 배열을 생성하고, 출력할 땐 거꾸로
# 예) [0, 1, 2, 3] => 3210
# 1씩 증가시킬 계획
answer = [-1]

# 목표 값만큼 반복
while N:
    # 일단 하나 찾음
    N -= 1
    
    # 맨 처음 1 올리기
    answer[0] += 1

    # 옆자리 비교는 두 자리 이상부터
    if len(answer) == 1 and answer[0] < 10:
        continue
    
    # 맨 첫 자리부터
    digit_idx = 0
    while True:
        # 옆자리를 참고하는데, 그러려면 2자리 필요
        if len(answer) > 1:
            # 다음 자릿수가 현재보다 크면 정상
            if answer[digit_idx + 1] > answer[digit_idx]:
                break

            # 같거나 크면 다음 자리 올리기
            answer[digit_idx + 1] += 1

            # 현재 자리는 이전 자리보다 1 크게
            if digit_idx > 0:
                answer[digit_idx] = answer[digit_idx - 1] + 1
            else:
                answer[digit_idx] = 0

            # 다음 자리로 넘어가 확인
            digit_idx += 1

        # 자릿수 늘려야 할 때: 비교했는데 더 이상 증가시킬 수 없을 떄
        # => 맨 끝이 9보다 커야 할 때
        if answer[digit_idx] == 10:
            # 한 칸 늘리고 
            answer.append(0)
            # 줄어드는 순서대로 초기화
            for i in range(len(answer)):
                answer[i] = i
            break
        
        # 모든 자리를 확인해서, 다음 자리가 길이를 벗어나면 종료
        if digit_idx == len(answer) - 1:
            break

print(*answer[::-1], sep='')
