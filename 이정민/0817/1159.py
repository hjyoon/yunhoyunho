num = int(input())

cnt = [0]*123

name =[]
for i in range(num):
    name.append(input())

#ord(문자) chr(숫자)
#name[0]이 ~면 카운트+1

for i in range(num):
    cnt[ord(name[i][0])] += 1

jip = []
for j in range(123):
    if cnt[j] >= 5:
        jip.append(j)
        continue

if len(jip)==0:
    print('PREDAJA')



for k in range(len(jip)):
    print(chr(jip[k]),end='')