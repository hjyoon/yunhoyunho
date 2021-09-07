import sys
sys.stdin = open('input.txt')

def dfs(arr):
    global new_arr
    new_arr = []
    if len(arr) == 2:
        for i in range(2):
            print(arr[i], end='')
    else:
        for i in range(len(arr) - 1):
            if int(arr[i]) + int(arr[i + 1]) >= 10:
                new_arr += [int(arr[i]) + int(arr[i + 1]) - 10]
            else:
                new_arr += [int(arr[i]) + int(arr[i + 1])]
    dfs(new_arr)


N = list(input())
M = list(input())
arr = []
for i in range(8):
    arr += N[i]
    arr += M[i]
new_arr = []

try:
    dfs(arr)
except RecursionError:
    pass