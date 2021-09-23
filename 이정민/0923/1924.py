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
'''

x, y = map(int,input().split())

if x == 1: pass
elif x == 2: y += 31
elif x == 3: y += 59
elif x == 4: y += 90
elif x == 5: y += 120
elif x == 6: y += 151
elif x == 7: y += 181
elif x == 8: y += 212
elif x == 9: y += 243
elif x == 10: y += 273
elif x == 11: y += 304
elif x == 12: y += 334

if y%7 == 1: print('MON')
elif y%7 == 2: print('TUE')
elif y%7 == 3: print('WED')
elif y%7 == 4: print('THU')
elif y%7 == 5: print('FRI')
elif y%7 == 6: print('SAT')
elif y%7 == 0: print('SUN')