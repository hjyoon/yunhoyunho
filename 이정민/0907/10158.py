'''
오른쪽에 벽 있으면 왼쪽위로 이동함
if x>=N
위에 벽 있으면 왼쪽아래로 이동함
if y<0
아래에 벽 있으면 왼쪽위로 이동함
if y>=N
왼쪽에 벽 있으면 오른쪽 위로 이동함
if x<0

벽체크 , 델타
if not x < 0 and not y < 0 and not x >= N and not y >= N:
뒤집어서 생각해야 함
'''
w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())
cnt = []
while p < w:
    (p, q) = (p + 1, q + 1)
    cnt += [[p, q]]
while ----
    if p >= w:
        while q<h and p>0:
            (p,q) = (p-1, q+1)
            cnt += [[p,q]]

    if q ==h :
        while p>0 and q>0:
            (p,q) = (p-1,q-1)
            cnt += [[p,q]]

    if q == 0:
        while p>0 and q>0:
            (p,q) = (p-1,q+1)
            cnt += [[p,q]]

    if p == 0:
        while q < h and p>0:
            (p, q) = (p + 1, q + 1)
            cnt += [[p,q]]
print(cnt[t-1])

# for i in range(t):
#     (p,q) = (p+1,q-1)
#     if p>=w:
#         (p,q) = (p-1,q-1)
#     if q<0:
#         (p,q) = (p-1,q+1)
#     if q>=h:
#         (p,q) = (p-1,q-1)
#     if p<0:
#         (p,q) = (p+1,q+1)
# print((p,q))







