from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


a_scores = list(map(int, input().split()))
b_scores = list(map(int, input().split()))
a_score_sum = 0
b_score_sum = 0
was_winning = False

for i in range(9):
    # 선공
    a_score_sum += a_scores[i]
    # 총 득점이 더 많은 경우 => 이기고 있던 순간
    if a_score_sum > b_score_sum:
        was_winning = True
        break
    
    # 후공
    b_score_sum += b_scores[i]

if was_winning:
    print('Yes')
else:
    print('No')
