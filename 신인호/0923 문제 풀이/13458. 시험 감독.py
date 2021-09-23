from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


import math


N = int(input())
applicant_list = list(map(int, input().split()))
chief_coverage, vice_coverage = map(int, input().split())
watcher_count = 0

for applicants in applicant_list:
    # 일단 총 감독관이 자기 할당량만큼 커버
    watcher_count += 1
    remain = applicants - chief_coverage

    # NOTE: 총 감독관이 전부 감시 가능한 경우도 있음...
    if remain > 0:
        # 필요한 감독관 수 = 나머지 인원 / 감독 가능한 수
        # 이때, 수가 모자라면 올림해야 함
        watcher_count += math.ceil(remain / vice_coverage)

print(watcher_count)
