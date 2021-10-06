N = int(input())
arr = [0]    # 3 3 1일때, 가장 첫번째인 3은 첫번째 선배가 되어야 하는데 리스트는 0번째부터 있으므로

cnt = 0
def sunbae(person):
    global cnt #몇명에게 물어봤는지
    if visit[person]:
        return  #만약 방문을 했던 곳에 또 갔으면? 끝
    if arr[person] and visit[person] == 0: # arr에 person인덱스가 있고 방문을 하지 않았으면
        visit[person] = 1 # 방문 표시
        cnt += 1      # 카운트
        person = arr[person]  # 방문한 곳에 해당하는 번호를 새로 갱신
        sunbae(person)       # 재귀

for i in range(N):
    arr.append(int(input()))

askcount = []

for i in range(len(arr)):   # 주어진 선배들에게 차례대로 함수를 사용하기 위함
    cnt = 0                 # cnt 초기화
    visit = [0] * (N+1)     # 방문도 초기화
    sunbae(i)                  # 함수
    askcount.append(cnt)         # dfg라는 빈 리스트에 각각의 경우에 갔을 때 몇명이나 물어봤는지 기록

for i in range(len(askcount)):
    if askcount[i] == max(askcount):
        print(i)
        break


