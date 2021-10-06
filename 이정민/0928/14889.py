N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]


#itertools combination, zip 함수

TeamsHave0 = []
for i in range(N):
    for j in range(N):
        if i >= j:
            TeamsHave0.append(arr[i][j] + arr[j][i])
        else:
            pass
print(TeamsHave0)


Teams = []
for i in range(len(TeamsHave0)-1):
    if TeamsHave0[i] != 0:
        Teams.append(TeamsHave0[i])
print(Teams)

minTeam = []
for i in range(len(Teams)):
    for j in range(i+1,len(Teams)):
        minTeam.append(abs(Teams[j]-Teams[i]))

print(minTeam)