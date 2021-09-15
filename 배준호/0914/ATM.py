import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
sum = 0
for i in range(N):
    sum += int(arr[i]) * (N-i)

print(sum)