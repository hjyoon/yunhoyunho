from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

total_wait = 0
cur_wait = 0
for i in arr:
    cur_wait += i
    total_wait += cur_wait

print(total_wait)