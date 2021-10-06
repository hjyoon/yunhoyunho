jeminis = list(map(int, input().split()))
startlink = list(map(int, input().split()))

j = 0 # jeminis의 점수 합
s = 0 # startlink의 점수 합
cnt = 0 # jeminis가 앞설 때가 한번이라도 존재하면 cnt != 0
for i in range(9):
    j += jeminis[i]
    if j > s:
        cnt+=1
    s += startlink[i]
'''
초, 말로 나누어 지는 것이므로
만약 8회 말까지 동점인데, 9회 초에서 j 가 득점을 하면 j가 이기고 있던 것이 된다.
그 상황에서 s가 j보다 더 많은 득점을 하면 s가 역전승을 한 꼴이 된다.
'''

if j < s :
    if cnt == 0:
        print('No')
    elif cnt > 0:
        print('Yes')
else:
    print('No')
    