'''
총 N개의 시험장, i번 시험장에 있는 응시자의 수는 Ai

총감독관은 한 시험장에서 감시할 수 있는 응시자의 수 B
부감독관은 한 시험장에서 감시할 수 있는 응시자의 수 C

총 감독관은 시험장마다 1명, 부감독관은 여러명

감독관 수의 최솟값은?
'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

# 먼저 각 시험장 응시자 수에 총감독관의 감시수 B를 뺀 뒤 cnt+=1
cnt = N
for i in A:
    i -= B
    if i == 0 or i < 0:
        continue
# 남은 응시자 수를 부감독관의 감시수 C로 나누고, 나눈 값이 0일 때와 0이 아닐 때로 구분지어 계산
    if i % C:
        cnt += i//C + 1
    else:
        cnt += i//C
print(cnt)