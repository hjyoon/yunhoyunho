arr = [list(map(int,input().split())) for i in range(5)]

max = 0
for i in range(len(arr)):
    if max < sum(arr[i]):
        max=sum(arr[i])
        cook = i+1

print(cook, max)