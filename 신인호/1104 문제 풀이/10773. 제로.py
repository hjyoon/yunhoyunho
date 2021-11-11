from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
스택
"""

K = int(input())
stack = [0] * K
idx = 0

for _ in range(K):
    num = int(input())
    if num:
        stack[idx] = num
        idx += 1
    else:
        if idx:
            idx -= 1

print(sum(stack[:idx]))
