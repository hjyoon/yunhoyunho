import sys
sys.stdin = open('input.txt')

def day(M, D):
    if M == 1:
        if D % 7 == 0:
            print('SUN')
        if D % 7 == 1:
            print('MON')
        if D % 7 == 2:
            print('TUE')
        if D % 7 == 3:
            print('WED')
        if D % 7 == 4:
            print('THU')
        if D % 7 == 5:
            print('FRI')
        if D % 7 == 6:
            print('SAT')
    else:
        if M == 2:
            D += 31
            day(M-1, D)
        elif M == 3:
            D += 28
            day(M-1, D)
        elif M == 4:
            D += 31
            day(M-1, D)
        elif M == 5:
            D += 30
            day(M-1, D)
        elif M == 6:
            D += 31
            day(M-1, D)
        elif M == 7:
            D += 30
            day(M-1, D)
        elif M == 8:
            D += 31
            day(M-1, D)
        elif M == 9:
            D += 31
            day(M-1, D)
        elif M == 10:
            D += 30
            day(M-1, D)
        elif M == 11:
            D += 31
            day(M-1, D)
        elif M == 12:
            D += 30
            day(M-1, D)



M, D = map(int, input().split())
day(M, D)