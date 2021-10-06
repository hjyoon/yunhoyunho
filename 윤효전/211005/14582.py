import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


t1_score = tuple(map(int, input().split()))
t2_score = tuple(map(int, input().split()))
t1_ac = 0
t2_ac = 0

sw = False

for i in range(9):
    t1_ac += t1_score[i]
    if t1_ac > t2_ac:
        sw = True
        break
    t2_ac += t2_score[i]

if sw:
    print('Yes')
else:
    print('No')
