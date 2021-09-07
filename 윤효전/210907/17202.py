from os import sep
from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

tmp = []
for i in range(8):
    tmp.append(int(A[i]))
    tmp.append(int(B[i]))

while len(tmp) > 2:
    tmp_new = []
    for i in range(len(tmp)-1):
        tmp_new.append((tmp[i] + tmp[i+1]) % 10)
    tmp = tmp_new

print(*tmp, sep='')
