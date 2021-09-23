num1 = list(input())
num2 = list(input())

arr = []
for i in range(8):
    arr.append(num1[i])
    arr.append(num2[i])

while len(arr) >= 3:
    asd = []
    for i in range(len(arr)-1):
        asd.append(int(arr[i])+int(arr[i+1]))
    arr = asd
if arr[0]%10*10 + arr[1]%10 >= 10:
    print(arr[0]%10*10 + arr[1]%10)
if arr[0]%10*10 + arr[1]%10 == 0:
    print(00)
if arr[0]%10*10 + arr[1]%10 < 10:
    ff = str((arr[0]%10*10 + arr[1]%10) * 10)
    print(ff[::-1])
