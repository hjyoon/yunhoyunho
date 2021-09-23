N = int(input())
arr = []
for i in range(N):
    asd = [list(input()) for _ in range(5)]
    arr.append(asd)
    # for i in range()
    #     if arr1[i][j] == arr2[i][j]:
    #         cnt+=1
def comparemap(arr, brr):
    cnt = 0
    for i in range(5):
        for j in range(7):
            if arr[i][j] != brr[i][j]:
                cnt += 1
    return cnt

min = 123456789
minarr1=0
minarr2=0
for i in range(N):
    for j in range(i+1,N):
        val = comparemap(arr[i], arr[j])
        if val < min:
            min = val
            minarr1=i
            minarr2=j

print(minarr1 + 1,end=' ')
print(minarr2 + 1)

