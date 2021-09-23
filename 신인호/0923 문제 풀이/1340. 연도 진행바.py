from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


MONTH_NUM = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
DAYS_OF_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
# 진행률 100% = 365일
# NOTE: 일 단위만으로는 부족하고 분도 포함해야 함
# NOTE: 왜 23:59분이 아니라 24:00가 기준...?
FULL_PROGRESS = 365 * 24 * 60


month, day, year, time = input().split()
month = MONTH_NUM[month[:3]]
day = int(day[:-1])
year = int(year)
hour, minute = map(int, time.split(':'))

# 이전까지의 달에 있던 일수를 전부 더함
for prev_month in range(1, month):
    day += DAYS_OF_MONTH[prev_month]

# NOTE: 윤년이면 2월이 29일이므로, 1일을 더 추가
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    # NOTE: 최대 일수는 증가시키되,
    # 현재 일수는 2월 넘길 때만
    FULL_PROGRESS += 24 * 60
    if month > 2:
        day += 1

# 전부 분 단위로 바꾼다.
minute += (day - 1) * 24 * 60 + hour * 60

# 현재 / 기준량의 비율을 구한다.
ratio = minute * 100 / FULL_PROGRESS
print(ratio)
