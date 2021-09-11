from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


CYCLE = 15 + 13
AXIS = 15

T = int(input())
for _ in range(T):
    N = int(input())
    
    # 몇 번째 차례인지
    # NOTE: 1부터 시작하면 아래와 같이 -1 하고 뒤에서 +1을 해야 함
    # 그래야 주기의 마지막 숫자가 주기로 나눠떨어지지 않음
    order = (N - 1) % CYCLE + 1
    # 15를 기준으로 양옆이 같음 
    # -> 15 넘으면 더 작은 쪽으로 오도록 만듦
    number = min(order, 2 * AXIS - order)
    
    # 이진수 함수
    binary_number = bin(number)[2:]
    # 이진수 앞쪽을 0으로 채우기
    binary_number = '0' * (4 - len(binary_number)) + binary_number

    # 단순히 0을 V로, 1을 딸기로 치환
    binary_strawberry = binary_number.replace('0', 'V').replace('1', '딸기')
    print(binary_strawberry)
