from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
매번 각 정점을 출발점으로 삼고, 쭉쭉 나아가면서 경로 길이 계산

안 될 거 같은 전략
- 거꾸로 거슬러가기 => 그게 그거
- 각 점마다 최대 길이를 저장 (메모이제이션) 
    => 출발점이 달라 진행 방향이 바뀌면? 저장된 정보 쓸모없어짐

될 거 같은 전략
- 방향과 길이를 같이 저장?
"""


def dfs(v_in, cur_len):
    global final_len
    # 한 명만 지목 가능 => 도착점은 딱 하나.
    v_out = arrivals[v_in]
    
    # base case: 갈 수 있는 곳을 방문했으면 더 이상 못 감
    if visited[v_out]:
        final_len = cur_len
    
    # 갈 수 있으면 방문 체크 후, 진행하고, 갔다와서 다시 방문 풀어 줌
    else:
        visited[v_out] = True
        dfs(v_out, cur_len + 1)
        visited[v_out] = False


# 선배의 수와, 선배들이 어떤 사람을 가리키는지를 입력받음
N = int(input())
arrivals = [0] + [int(input()) for _ in range(N)]

# 방문 체크 배열과, 길이를 담을 전역변수를 선언
visited = [False] * (N + 1)
final_len = 0
max_len = 0
max_index = 0

# 모든 점을 출발점으로 삼아야 함 (끊기는 경우도 있기 때문)
for v_in in range(1, N + 1):
    # 한 점을 출발점으로 삼고, 그때의 최대 경로 길이를 구함
    visited[v_in] = True
    dfs(v_in, 0)
    visited[v_in] = False

    # 기존보다 클 때만 최댓값 갱신
    if final_len > max_len:
        max_len = final_len
        max_index = v_in

print(max_index)
