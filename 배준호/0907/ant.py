import sys
sys.stdin = open('input.txt')
def dfs(p, q, t):
    if t == 0:
        return (p, q)
    else:
        if w-p > h-q:
            p += h-q
            q += h-q
            t -= h-q
        else:
            p += w-p
            q += w-p
            t -= w-p


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
arr = [[0] * w for _ in range(h)]
print(dfs(p, q, t))