import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def check_dots_in_rectangle(x_min, x_max, y_min, y_max):
    # 주어진 정사각형 안에 모든 점이 들어올 수 있는지 체크

    # 각각의 점들에 대해
    for dot in dots:
        x, y = dot

        # 1. 정사각형의 범위 안에 있고
        # 2. x축이나 y축 중 하나에 속하면 됨
        if x_min <= x <= x_max and y_min <= y <= y_max \
            and (x == x_min or x == x_max or y == y_min or y == y_max):
            continue
        # 그렇지 않으면 변 위에 없음
        else:
            return False
    
    # 전부 정사각형 변 위에 있었으면 True
    return True


dot_num = int(input())
dots = [list(map(int, input().split())) for _ in range(dot_num)]
 
# 각각의 축 방향으로 가장 멀리 떨어진 점들을 구한다.
x_min = x_max = dots[0][0]
y_min = y_max = dots[0][1]

for dot in dots:
    x, y = dot

    x_max = max(x, x_max)
    x_min = min(x, x_min)

    y_max = max(y, y_max)
    y_min = min(y, y_min)

# 어느 축이 가장 멀리 떨어져 있는지를 구한다.
# -> 그 축이 곧 정사각형의 최대 길이가 된다.
length = 0
if x_max - x_min > y_max - y_min:
    length = x_max - x_min
    # 다른 쪽 축은, y의 최댓값이나 최솟값 중 하나가 변에 속한다.
    # 한쪽을 변으로 정하면, 마주보는 변의 위치 또한 정할 수 있다.
    # 모든 변의 위치를 아니까 정사각형을 정할 수 있고,
    # 이 정사각형에 점이 있는지를 체크할 수 있다.
    result1 = check_dots_in_rectangle(x_min, x_max, y_max - length, y_max)
    result2 = check_dots_in_rectangle(x_min, x_max, y_min, y_min + length)
else:
    length = y_max - y_min
    result1 = check_dots_in_rectangle(x_max - length, x_max, y_min, y_max)
    result2 = check_dots_in_rectangle(x_min, x_min + length, y_min, y_max)

if result1 or result2:
    print(length)
else:
    print(-1)