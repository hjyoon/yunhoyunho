N, M = input().split()

asd = []
for i in range(len(N)):
    if N[i] == '1':
        asd.append(2**(len(N)-i-1))
sum1 = sum(asd)

sdf = []
for i in range(len(M)):
    if M[i] == '1':
        sdf.append(2**(len(M)-i-1))
sum2 = sum(sdf)

sum3 = sum1+sum2

qwe = []
for i in range(85):
    qwe.append(sum3 % 2)
    sum3 = sum3 // 2

    if sum3 == 0:
        break

qwe.reverse()
for i in range(len(qwe)):
    print(qwe[i],end='')