import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = map(int, input().split())
B, C = map(int, input().split())

ans = 0
for v in S:
    ans += 1
    if v < B:
        continue
    v -= B
    if v % C == 0:
        ans += (v // C)
    else:
        ans += (v // C) + 1
print(ans)
