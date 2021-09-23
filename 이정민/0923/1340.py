'''
2월 = +31
3월 = +59
4월 = +90
5월 = +120
6월 = +151
7월 = +181
8월 = +212
9월 = +243
10월 = +273
11월 = +304
12월 = +334

위의 값*24 + 날짜*24 + 년도무시 + 시간
시간은 그대로 더하고, 시간 뒤의 값은 60으로 나눠서 더해주면 된다.

다 더한 값을 365*24로 나누고 *100 해주면 되려나
'''
time = []
now = input().split()
time.append(now[0])
time.append(int(now[1][0:-1]))
time.append(now[3].split(':'))

yoon = [2000,2400]
for i in range(1800, 2601):
    if i%4 == 0 and i%100 != 0:
       yoon.append(i)
print(time)
if int(now[2]) in yoon:
    if time[0] == 'January': time[1] -= 1
    elif time[0] == 'February':time[1] += 30
    elif time[0] == 'March':time[1] += 59
    elif time[0] == 'April':time[1] += 90
    elif time[0] == 'May':time[1] += 120
    elif time[0] == 'June':time[1] += 151
    elif time[0] == 'July':time[1] += 181
    elif time[0] == 'August':time[1] += 212
    elif time[0] == 'September': time[1] += 243
    elif time[0] == 'October':time[1] += 273
    elif time[0] == 'November':time[1] += 304
    elif time[0] == 'December':time[1] += 334
    print((time[1] * 24 * 60 + int(time[2][0]) * 60 + int(time[2][1])) / (366 * 24 * 60) * 100)
else:
    if time[0] == 'January': time[1] -= 1
    elif time[0] == 'February': time[1] += 30
    elif time[0] == 'March': time[1] += 58
    elif time[0] == 'April': time[1] += 89
    elif time[0] == 'May': time[1] += 119
    elif time[0] == 'June': time[1] += 150
    elif time[0] == 'July': time[1] += 180
    elif time[0] == 'August': time[1] += 211
    elif time[0] == 'September': time[1] += 242
    elif time[0] == 'October': time[1] += 272
    elif time[0] == 'November': time[1] += 303
    elif time[0] == 'December': time[1] += 333
    print((time[1] * 24 * 60 + int(time[2][0]) * 60 + int(time[2][1])) / (365 * 24 * 60) * 100)
    #print(((time[1] * 24 + int(time[2][0]) + int(time[2][1]) / 60) / (365 * 24)) * 100)





'''
윤년 : 2000, 2400 / 4로 나누어 떨어지면서 100으로 나누어 떨어지지 않는 해
'''