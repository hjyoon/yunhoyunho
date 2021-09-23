from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def is_leap_year(year):
    ret = None
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        ret = True
    else:
        ret = False
    return ret


d = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

day_list = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

S = input().rstrip().replace(',', '').replace(':', ' ').split()

year = int(S[2])
month = d[S[0]]
day = int(S[1])
hour = int(S[3])
minute = int(S[4])

# 윤년인 경우 True
if is_leap_year(year):
    day_list[2] = 29

total = 60*24*sum(day_list[1:13])
#print(total, sum(day_list[1:13]))
now = minute + 60*hour + 60*24*(day-1) + 60*24*sum(day_list[1:month])
# print(now)

print(now / total * 100)
