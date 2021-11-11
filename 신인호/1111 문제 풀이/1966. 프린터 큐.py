from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
큐에 (중요도, 초기 위치값)을 같이 넣기.
인쇄할지 말지는 중요도를 비교하고,
인쇄하고 나서는 초기 위치값을 비교.
"""

T = int(input())
for test_case in range(T):
    page_num, wanted = map(int, input().split())
    pages = enumerate(map(int, input().split()))

    # 원형 큐 사용
    size = 2 * page_num
    Q = [[] for _ in range(size)]
    front = -1
    rear = page_num - 1

    # 큐에 원소 전부 채워놓기
    for idx, value in pages :
        Q[idx] = (value, idx)

    page_order = 0
    # 큐가 빌 때까지
    while front != rear:
        # 큐의 첫 번째 원소 뽑기
        front = (front + 1) % size
        value, idx = Q[front]

        cur = front
        # 다음 원소부터 마지막 원소까지 순회
        while cur != rear:
            # NOTE: rear 전에 +1 하니까, rear까지 해당
            cur = (cur + 1) % size
            # 중요도 비교 후, 높은 게 있으면 뒤에 넣기
            if Q[cur][0] > value:
                rear = (rear + 1) % size
                Q[rear] = (value, idx)
                break
        # 중요도 높은 게 없으면 프린트 출력
        else:
            page_order += 1 
            # 원하는 인덱스면 번호 출력 후 시행 종료
            if idx == wanted:
                print(page_order)
                break
