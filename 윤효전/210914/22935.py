from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
l = list(range(1, 16)) + list(range(14, 1, -1))

for _ in range(1, T+1):
    N = int(input())
    N = ((N-1) % 28)
    tmp = bin(l[N])[2:].zfill(4)
    for c in tmp:
        print(['V', '딸기'][int(c)], end='')
    print()
