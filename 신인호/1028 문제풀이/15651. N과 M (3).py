from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def nTTr(n, r, k):
    if k == r:
        print(*arr)
    else:
        for i in range(n):
            arr[k] = i + 1
            nTTr(n, r, k + 1)   # 시작값 제거
                                # 어차피 처음부터 시작


N, M = map(int, input().split())
arr = [0] * M
nTTr(N, M, 0)