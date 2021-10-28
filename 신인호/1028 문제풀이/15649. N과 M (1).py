from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def nPr(n, r, k):
    if k == r:
        print(*arr)
    else:
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                arr[k] = i
                nPr(n, r, k + 1)
                used[i] = False

N, M = map(int, input().split())
arr = [0] * M
used = [False] * (N + 1)

nPr(N, M, 0)