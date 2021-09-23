import sys
sys.stdin = open('input.txt')

# 월을 날짜로 합한 함수
def month_to_int(a):
    if a == 'January':
        return 0
    elif a == 'February':
        return 31
    elif a == 'March':
        return 31+28
    elif a == 'April':
        return 31+28+31
    elif a == 'May':
        return 31+28+31+30
    elif a == 'June':
        return 31+28+31+30+31
    elif a == 'July':
        return 31+28+31+30+31+30
    elif a == 'August':
        return 31+28+31+30+31+30+31
    elif a == 'September':
        return 31+28+31+30+31+30+31+31
    elif a == 'October':
        return 31+28+31+30+31+30+31+31+30
    elif a == 'November':
        return 31+28+31+30+31+30+31+31+30+31
    elif a == 'December':
        return 31+28+31+30+31+30+31+31+30+31+30

#윤년 확인 합수
def yoon(b):
    if int(b) % 400 == 0:
        return True
    elif int(b) % 4 == 0 and int(b) % 100 != 0:
        return True
    else:
        return False

N = list(input().split())
day = 0

# 월을 날짜로 합한 값
if yoon(N[2]):
    if N[0] != 'January' and N[0] != 'February': 
        day += month_to_int(N[0]) + 1
else:
    day += month_to_int(N[0])

# 날짜 추가
day += int(N[1].replace(',','')) - 1

# 시간을 퍼센트로
T = list(map(int, (N[3].replace(':', ' ')).split()))
day += ((T[0]+ (T[1] / 60))/ 24)

# 퍼센트 계산
if yoon(N[2]):
    print(day/366 * 100)
else:
    print(day/365 * 100)
