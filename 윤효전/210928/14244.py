import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

for i in range(N-1-(M-2)):
    print(i, i+1)

for j in range(i+1, N-1):
    print(i, j+1)
