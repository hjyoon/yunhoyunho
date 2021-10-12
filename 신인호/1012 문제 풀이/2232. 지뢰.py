from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
< 지뢰가 터질 때 >

A. 현재보다 오른쪽이 작으면 터짐. 
단, 첫 번째 폭탄 이후 지점들은 괜찮음
    - 1 {2}  1
    - 1 {3}  2 1 ...

B. 현재랑 오른쪽이 같으면 무조건 터짐.
    - 1 {2}  2  3 ...
    - 1 {2} {2} 2 ...

A + B. 오른쪽이랑 같지만 감소하는 추세의 지점은 괜찮음
(이전 폭탄의 사거리 내이기 때문)
    - 1 {2}  1 {1} 1 ...
"""


N = int(input())
# FIXME: 1부터 시작하기 위해 앞에 0 추가
arr = [0] + [int(line) for line in sys.stdin]
mine_list = []

# 수열의 증가/감소 추세를 알려주는 플래그
# 처음으로 감소하는 부분의 지뢰만 터트릴 예정
is_decreasing = False

for i in range(1, N):
    # 숫자가 줄어드는 지점인 경우
    if arr[i] > arr[i + 1]:
        # 계속 증가하는 추세였던 경우
        if not is_decreasing:
            # 증가하다 감소하는 점 => 최댓값이므로 추가
            mine_list.append(i)
            # 감소하는 흐름임을 플래그로 표시
            is_decreasing = True
        # 다음에 작은 게 와도, 이미 감소 중인 걸 앎
        # 이때는 연쇄 폭발 가능하므로, 그냥 넘어감
    else:
        # 숫자가 옆 숫자랑 같고, 감소하는 추세가 아니어야 함
        # <- 감소하는 추세인 경우엔, 이미 연쇄 폭발 범위이기 때문
        if arr[i] == arr[i + 1] and not is_decreasing:
            mine_list.append(i)
        # 옆 숫자가 더 크거나 같으면 감소하는 추세는 아님
        is_decreasing = False

# FIXME: 마지막 폭탄은 따로 처리
# 이전보다 같거나 '더 크면' 터져야 함
if arr[N - 1] <= arr[N]:
    mine_list.append(N)

print(*mine_list, sep='\n')
