

'''
arr = '총글자길이'
target = '찾는거'
N = len(arr)
M = len(target)

flag = 0
for i in range(N-M+1):
    flag = 0
    for j in range(M):
        if arr[i+j] != target[j]:
            flag = 1
            break
    if flag == 0:
        break
'''
cro = input()
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = len(cro)


cnt = 0
flag = 0
for word in words:
    M = len(word)
    for i in range(N-M+1):
        flag = 0
        for j in range(M):
            if cro[i+j] != word[j]:
                flag = 1
                continue
        if flag == 0:
            cnt += 1
            for m in range(i,M+i):
                cro.replace()
print(cnt)
print(cro)