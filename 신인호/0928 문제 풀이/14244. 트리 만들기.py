from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
리프 개수만큼 한 개씩 늘리다가
마지막 노드는 리프 개수를 유지하며 쭉 늘리기
"""

# T = 4
# for test_case in range(T):
N, M = map(int, input().split())

# 무조건 첫 리프는 0, 루트는 1
last, start = 0, 1
print(last, start)

# 노드 두 개를 찍었으므로 2개 줄이고,
# 리프 한 개 나왔으므로 1개 줄이고,
# 다음 리프를 위해 1 증가
N -= 2
M -= 1
last = 1

while N > 0:
    # 리프가 더 필요한 경우
    if M > 0:
        # 1은 가만 놔두고 가지치기
        # 리프 노드는 늘어나고, 필요 개수는 줄어듦
        last += 1
        M -= 1
    else:
        # 리프가 더 이상 필요없으면
        # 이전 리프가 시작점 -> 계속 이어짐.
        start, last = last, last + 1
    print(start, last)
    # 필요한 노드 개수 한 개 줄임
    N -= 1
