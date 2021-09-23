tem = []
for i in range(987654321) :
   num = float(input())
   if (num == 999):
       break
   tem.append(num)

rst = []
for i in range(len(tem)-1):
        rst+= ['%0.2f' % (float(tem[i+1] - tem[i]))]

for i in rst:
    print(i)