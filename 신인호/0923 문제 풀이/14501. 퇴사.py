from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
핵심: 바로 이전까지의 최댓값 vs. (현재 값 + 이전 구간 합)

예)
날짜: 1 2 3 4 5 6 7 8 9 10
기간: 1 2 3 4 5 1 2 3 4 5
보수: 1 2 3 4 5 4 5 1 2 3 4 5 인 경우의 
가능한 최대 합은

날짜:  10 9 8 7 6 5 4 3 2 1
기간:   5 4 3 2 1 5 4 3 2 1
구간합: 0 0 3 3 4 5 7 7 9 10 과 같다.

8일째: 이때부터 상담 가능. 현재 최대 합은 3.
7일째: 안 하는 게 이득이므로, 여전히 3이 최대이다.
6일째: 1일짜리니까 할 수 있음. 최대 합은 4.
5일째: 5일째 상담을 하는 게 이득이다.
    6일째와 8일째를 포기하고, 대신 5를 얻는다.
4일째: 5일째 상담을 선택하면 최대 합은 5가 된다.
    그러나 4일 전 (8일째까지의) 최대 합 
    + 4일째 상담 (4일째 ~ 7일째) 비용은
    3 + 4가 되어 최대 합이 7이 된다.
    
    이는 5일째까지의 최대 합인 5보다 크므로,
    5일째를 포기하고 4일째 상담을 선택해야 한다.

이후 비슷한 방식으로 진행
"""

TIME = 0
REWARD = 1

N = int(input())
counsels = [list(map(int, input().split())) for _ in range(N)]
max_reward = [0] * (N + 1)

for day in range(N - 1, -1, -1):
    counsel_end_day = day + counsels[day][TIME]

    # 상담 기간이 마지막 날을 초과하는 경우엔 상담 안 함.
    # 이때는 이전까지의 구간 합이 그대로 이어짐.
    if counsel_end_day > N:
        max_reward[day] = max_reward[day + 1]
        continue

    # 이전까지의 최대 합
    prev_max = max_reward[day + 1]
    # 오늘 상담 비용 + 상담 기간 이전의 최대 합
    this_max = counsels[day][REWARD] + max_reward[counsel_end_day]

    if this_max >= prev_max:
        max_reward[day] = this_max
    else:
        max_reward[day] = prev_max

print(max_reward[0])