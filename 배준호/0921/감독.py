import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(N):
    if (A[i]-B) % C == 0:
        cnt += 1 + (A[i]-B)//C
    else:
        cnt += 1 + (A[i]-B)//C + 1

print(cnt)