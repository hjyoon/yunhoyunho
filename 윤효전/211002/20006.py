import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_room(l, room, m):
    ret = -1
    for i in range(len(room)):
        first_player = room[i][0]
        if abs(first_player[0]-l) <= 10 and len(room[i]) < m:
            ret = i
            break
    return ret


P, M = map(int, input().split())
room = []
for i in range(P):
    l, n = input().split()
    l = int(l)
    idx = find_room(l, room, M)
    if idx == -1:
        room.append([(l, n)])
    else:
        room[idx].append((l, n))

for p_list in room:
    p_list.sort(key=lambda x: x[1])
    if len(p_list) == M:
        print('Started!')
    else:
        print('Waiting!')
    for p in p_list:
        print(*p)
