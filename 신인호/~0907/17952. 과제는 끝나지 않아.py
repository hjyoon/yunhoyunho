import sys
input = sys.stdin.readline


N = int(input().rstrip())
score_sum = 0
scores = []
minutes = []

for _ in range(N):
    assignment = list(map(int, input().split()))
    if assignment[0]:
        scores.append(assignment[1])
        minutes.append(assignment[2])

    # NOTE: 과제가 처음에 안 주어지는 경우도 있음
    if minutes:
        minutes[-1] -= 1

        if not minutes[-1]:
            score_sum += scores.pop()
            minutes.pop()

print(score_sum)