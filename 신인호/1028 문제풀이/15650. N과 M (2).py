from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def nCr(n, r, k, start):
    if k == r:
        print(*arr)
    else:
        for i in range(start, n):
            arr[k] = i + 1
            nCr(n, r, k + 1, i + 1)


N, M = map(int, input().split())
arr = [0] * M
nCr(N, M, 0, 0)
