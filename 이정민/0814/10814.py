N = int(input())

jip = [list(input().split()) for _ in range(N)]
jip = sorted(jip, key=lambda x:int(x[0]))

for i in range(N):
    print(jip[i][0],jip[i][1])