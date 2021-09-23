from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


DAYS_OF_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
DAY_NAMES = [
    'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'
]

month, day = map(int, input().split())

# 이전까지의 달에 있던 일수를 전부 더함
for prev_month in range(1, month):
    day += DAYS_OF_MONTH[prev_month]

# 전체 일수를 7로 나누면 현재 몇 번째 요일인지 알 수 있음
# 이때, 0 대신 1일부터 시작했으므로 1을 빼줘야 함
weekday = (day - 1) % 7

print(DAY_NAMES[weekday])
