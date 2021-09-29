from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


from itertools import combinations


def sum_team_value(team):
    team_value = 0
    # (1, 3, 6)인 경우, 1&3, 1&6, 3&6 각 쌍의 합을 구함.
    # 각 쌍의 합을 모두 더하면, 팀 전체의 합이 나옴.
    for a in range(len(team) - 1):
        for b in range(a, len(team)):
            team_value += sum_table[team[a]][team[b]]
    return team_value


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 능력치 합 테이블 만들기 => 반복 계산 줄이기
sum_table = [[0] * N for _ in range(N)]
for x in range(N - 1):
    for y in range(x + 1, N):
        sum_table[x][y] = arr[x][y] + arr[y][x]

# 2. 조합 리스트
team_list = list(combinations(range(N), N//2))
full_member = set(range(N))

# 3. 계산한 팀들은 set에 추가하고, 
# set에 없는 것들만 계산
checked_team_set = set()

min_diff = 1e9
for team in team_list:
    # 이미 계산한 팀들은 제외
    if team in checked_team_set:
        continue
    
    # 차집합을 이용해 다른 팀을 구함
    other_team = tuple(full_member - set(team))

    # 팀의 능력치 합의 차이를 구해서, 현재 최솟값과 비교
    diff = abs(sum_team_value(team) - sum_team_value(other_team))
    min_diff = min(min_diff, diff)

    # 둘 다 제외해서, 팀의 능력치 합 구하는 중복 연산을 줄임
    checked_team_set.add(team)
    checked_team_set.add(other_team)

print(min_diff)
