import itertools
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


N = int(input().rstrip())
S = [list(map(int, s.rstrip().split())) for s in sys.stdin]
l = tuple(range(1, N+1))
c = tuple(itertools.combinations(l, N//2))
c = tuple(zip(c[:len(c)//2], c[:len(c)//2-1:-1]))
r = 99999
for v in c:
    a, b = v
    a = sum(map(lambda x: S[x[0]-1][x[1]-1]+S[x[1]-1]
            [x[0]-1], itertools.combinations(a, 2)))
    b = sum(map(lambda x: S[x[0]-1][x[1]-1]+S[x[1]-1]
            [x[0]-1], itertools.combinations(b, 2)))
    r = min(r, abs(a-b))
