from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
N과 M이 각각 100000까지 가능
- 일반적인 이중반복문으로 찾으려면 O(N^2) -> 100억 -> 최소 10초

- 반면 이진탐색을 이용하면
    N 정렬 -> O(N log N) -> 100000 * 대략 17 = 170만
    M 이진탐색 -> O(M log N) -> 약 170만
    결과적으로 340만이 되어, 무난히 찾을 수 있음 
"""


N = int(input())
# 정렬
numbers = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

# 이진탐색 (M log N : 전체 M개에 대해, 각각 log N 만큼 소요)
for target in targets:
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] < target:
            # 범위를 한 칸씩 줄이거나 늘리는 게 핵심
            # 안 하면 계속 같은 자리만 걸려서 무한 루프 돌 수 있음
            left = mid + 1
        elif numbers[mid] > target:
            right = mid - 1
        else:
            print(1)
            break
    else:
        print(0)
