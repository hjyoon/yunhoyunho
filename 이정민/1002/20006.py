p, m = map(int,input().split())

players = []
for i in range(p):
    players.append(input().split())

roooms = []
def room(player):
    if len(player) < m:
        asd = []
        while len(player):
            j = 0
            asd.append(player[j])
            del player[j]
        roooms.append(asd)
        return

    rooms = []
    rooms.append(player[0])
    #
    # if len(player) == 1:
    #     roooms.append(player)
    #     return
    i = 1
    while len(rooms)<m:
        if abs(int(player[i][0]) - int(player[0][0])) <= 10:
            rooms.append(player[i])
            del player[i]
        else:
            i = i+1
        if len(rooms) == m:
            del player[0]
            roooms.append(rooms)
            room(player)

room(players)
for i in range(len(roooms)):
    if len(roooms[i]) == m:
        print('Started!')
        for j in range(len(roooms[i])):
            print('{} {}'.format(roooms[i][j][0], roooms[i][j][1]))
    else:
        print('Waiting!')
        for k in range(len(roooms[i])):
            print('{} {}'.format(roooms[i][k][0], roooms[i][k][1]))

'''
12 5
10 a
15 b
20 c
25 d
30 e
17 f
18 g
26 h
40 i
28 j
24 k
42 k

2 1
10 a
20 b
'''