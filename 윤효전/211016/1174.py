import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def makeNum(n, ac):
    ac.append(n)
    for i in range(-1, n):
        makeNum(i, ac)
        ans.add(''.join(map(str, ac)))
    ac.pop()


ans = set()
ac = []
for i in range(10):
    makeNum(i, ac)
ans = sorted(map(int, ans))
print(ans, len(ans))

N = int(input())
if N > len(ans):
    print(-1)
else:
    print(ans[N-1])
