import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a, b, c = map(int, input().split())
chk = [None] + [2] * (a+b+c)
n = int(input())
S = []
for _ in range(n):
    i, j, k, r = map(int, input().split())
    S.append((i, j, k, r))

S.sort(key=lambda x:-x[3])

for i, j, k, r in S:
    if r == 1:
        chk[i] = chk[j] = chk[k] = 1
    else:
        if (1, 1) == (chk[i], chk[j]):
            chk[k] = 0
        elif (1, 1) == (chk[i], chk[k]):
            chk[j] = 0
        elif (1, 1) == (chk[j], chk[k]):
            chk[i] = 0

print(*chk[1:], sep='\n')