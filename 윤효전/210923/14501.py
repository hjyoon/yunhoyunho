import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = [None]
for _ in range(N):
    T, P = map(int, input().split())
    S.append((T, P))
# print(S)

dp = [0] * (N+2)
ans = 0
for i in range(1, N+1):
    if i+S[i][0] <= N+1:
        dp[i+S[i][0]] = max(dp[i+S[i][0]], dp[i]+S[i][1])
        ans = max(ans, dp[i+S[i][0]])
    print(dp)
    dp[i+1] = max(dp[i+1], dp[i])
    ans = max(ans, dp[i+1])
    print(dp)
    print()

print(ans)
