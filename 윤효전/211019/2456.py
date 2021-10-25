import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
candidates = [{'1': 0, '2': 0, '3': 0, 'total': 0, 'num': i}
              for i in range(1, 4)]

for _ in range(N):
    a, b, c = input().rstrip().split()
    candidates[0][a] += 1
    candidates[0]['total'] += int(a)
    candidates[1][b] += 1
    candidates[1]['total'] += int(b)
    candidates[2][c] += 1
    candidates[2]['total'] += int(c)

candidates.sort(key=lambda x: (x['total'], x['3'], x['2']))
a, b = candidates[-1], candidates[-2]
if a['total'] != b['total']:
    print(a['num'], a['total'])
elif a['1'] != b['1']:
    print(a['num'], a['total'])
else:
    print(0, a['total'])
