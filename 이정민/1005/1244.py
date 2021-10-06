'''
*1은 스위치가 켜짐, 0은 스위치가 꺼짐
*남학생은 받은 스위치 번호의 배수들을 상태를 바꿈
*여학생은 자기가 받은 수를 중심으로, 좌우가 대칭인 양옆의 스위치들을 모두 바꿈

* 첫째 줄에는 스위치 개수
* 둘째 줄에는 스위치 상태
* 셋째 줄에는 학생 수
* 다음 줄에는 학생(남 1 여 2)과 받은 스위치 번호
'''

switches = int(input())
switch = list(map(int, input().split()))
students = int(input())
student = []
for i in range(students):
    templist = list(map(int,input().split()))
    student.append(templist)
# 1, 3 / 2, 3
for i in range(len(student)):
    #남학생인 경우 받은 스위치 번호의 배수들을 상태를 바꿈
    if student[i][0] == 1:
        for j in range(1,(switches//student[i][1])+1):
            if switch[(student[i][1]*j)-1] == 0:
                switch[(student[i][1]*j)-1] = 1
                continue
            if switch[(student[i][1]*j)-1] == 1:
                switch[(student[i][1]*j)-1] = 0
                continue

    # 여학생인 경우
    if student[i][0] == 2:
        # 주어진 스위치 값이 총 스위치 갯수의 절반보다 작으면
        if student[i][1] <= (switches + 1) // 2:
            for m in range(student[i][1]):
                if switch[student[i][1] - 1 - m] != switch[student[i][1] - 1 + m]:
                    break
                if switch[student[i][1] - 1 - m] == switch[student[i][1] - 1 + m]:
                    if switch[student[i][1] - 1 - m] == 0:
                        switch[student[i][1] - 1 - m] = 1
                        switch[student[i][1] - 1 + m] = 1
                        continue
                    if switch[student[i][1] - 1 - m] == 1:
                        switch[student[i][1] - 1 - m] = 0
                        switch[student[i][1] - 1 + m] = 0
                        continue

        # 절반보다 크면
        if student[i][1] > (switches + 1) // 2:
            if switches == student[i][1]:
                if student[i][1] == 0:
                    student[i][1] = 1
                if student[i][1] == 1:
                    student[i][1] = 0
            # 주의할점!!! range를 그냥 switches-student[i][1]로 해버리면,
            # 만약
            for m in range(switches - student[i][1]+1):
                if switch[student[i][1] - 1 - m] != switch[student[i][1] - 1 + m]:
                    break
                if switch[student[i][1] - 1 - m] == switch[student[i][1] - 1 + m]:
                    if switch[student[i][1] - 1 - m] == 0:
                        switch[student[i][1] - 1 - m] = 1
                        switch[student[i][1] - 1 + m] = 1
                        continue
                    if switch[student[i][1] - 1 - m] == 1:
                        switch[student[i][1] - 1 - m] = 0
                        switch[student[i][1] - 1 + m] = 0
                        continue


for i in range(len(switch)):
    if i > 0 and i % 20 == 0:
        print()
    print(switch[i], end=' ')

