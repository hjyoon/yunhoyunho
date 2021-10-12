from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
가까운 것들 중에서,
가장 가까운 것을 고른다.
"""

START = 0
END = 1

N = int(input())
meetings = [tuple(map(int, line.split())) for line in sys.stdin]
# FIXME: 종료 시간이 같을 땐 시작 시간 순으로 정렬해야 함
# <- 시작 시간과 종료 시간이 같은 게 먼저 오는 경우도 있기 때문
# 참고: https://www.acmicpc.net/board/view/74752
meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])


available = 0
end_time = 0
for i in range(N):
    if end_time <= meetings[i][START]:
        available += 1
        end_time = meetings[i][END]

print(available)
