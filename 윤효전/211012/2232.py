import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline


G_START = 0
# 리스트에서 가장 큰 값을 찾고 그 인덱스를 리턴
def find_largest(l, ordered_l):
    global G_START
    ret = 0
    for i in range(G_START, len(ordered_l)):
        idx = ordered_l[i][0]
        if l[idx] != 0:
            ret = idx
            break
    G_START = i+1
    return ret


def bomb_idx(l, idx):
    global N
    tmp_power = l[idx]
    left, right = idx-1, idx+1

    # 왼쪽으로 계속 터트린다
    while left > -1:
        if l[left] > 0 and l[left] < tmp_power:
            tmp_power = l[left]
            l[left] = 0
            left -= 1
            N -= 1
        else:
            break

    tmp_power = l[idx]

    # 오른쪽으로 계속 터트린다
    while right < len(l):
        if l[right] > 0 and l[right] < tmp_power:
            tmp_power = l[right]
            l[right] = 0
            right += 1
            N -= 1
        else:
            break

    l[idx] = 0
    N -= 1


ans = []
N = int(input())
S = [int(input()) for _ in range(N)]
# 터트릴 순서를 먼저 정렬해놓는다
ordered_S = sorted(enumerate(S), key=lambda x: -x[1])

while N > 0:
    idx = find_largest(S, ordered_S)
    ans.append(idx+1)
    bomb_idx(S, idx)

print(*sorted(ans))
