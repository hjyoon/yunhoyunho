# T = int(input())
# for tc in range(1,T+1):
#     num = int(input())
#
# # 15
#     def izin(num):
#         asd=[]
#         if num == 0:
#             return 'V'
#         if 0 < num <= 15:
#             while num > 1:
#                 if num % 2 == 0:
#                     asd += '0'
#                     num = num // 2
#                 elif num % 2 != 0:
#                     asd += '1'
#                     num = num // 2
#             if num == 1:
#                 return asd + ['1']
#             elif num == 0:
#                 return asd + ['0']
#
#         # -------------정방향-------------------------
#         if 16<= num <= 29:
#             num = num-15
#             while num > 1:
#                 if num % 2 == 0:
#                     asd += '0'
#                     num = num // 2
#                 elif num % 2 != 0:
#                     asd += '1'
#                     num = num // 2
#             if num == 1:
#                 return asd[::-1] + ['1']
#             elif num == 0:
#                 return asd[::-1] + ['0']
#
#
#         else:
#             if ((num-15)//14)%2!=0:
#
#
#
#             if (num // 15) % 2 != 0:
#                 num = 15 - (num % 15)
#
#                 while num > 1:
#                     if num % 2 == 0:
#                         asd += '0'
#                         num = num // 2
#                     elif num % 2 != 0:
#                         asd += '1'
#                         num = num // 2
#                 if num == 1:
#                     return asd + ['1']
#                 elif num == 0:
#                     return asd + ['0']
#             # ------------역방향---------------------------
#             elif (num // 15) % 2 == 0:
#                 num = num % 15
#                 # 31 32 33 = 15- 1  15 - 2  15- 3
#                 while num > 1:
#                     if num % 2 == 0:
#                         asd += '0'
#                         num = num // 2
#
#                     elif num % 2 != 0:
#                         asd += '1'
#                         num = num // 2
#                 if num == 1:
#                     return asd[::-1] + ['1']
#                 elif num == 0:
#                     return asd[::-1] + ['0']
#
#     # print(izin(num)[::-1])
#
#     sdf = []
#     for i in izin(num)[::-1]:
#         if i == '1':
#             sdf.append('딸기')
#         elif i == '0':
#             sdf.append('V')
#     if len(sdf) == 1:
#         print('V' + 'V' + 'V' + sdf[0])
#     elif len(sdf) == 2:
#         print('V'+'V'+sdf[0]+sdf[1])
#     elif len(sdf) == 3:
#         print('V' + sdf[0] + sdf[1] + sdf[2])
#     else:
#         for i in sdf:
#             print(i,end='')

# 테스트 케이스 입력
T = int(input())
for tc in range(1,T+1):
    # 주어지는 숫자를 입력받음
    num = int(input())
    # 15 이상이 되면 다시 되돌아오게 설정
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,14,13,12,11,10,9,8,7,6,5,4,3,2]
    # 0인 경우는 딸기가 없이 박자만 나오게 설정
    if num == 0:
        print('VVVV')
    elif num > 0:
        num = num % 28
        asd = list(bin(arr[num-1]))

    # bin 함수를 쓰면 0b---- 식으로 나오므로 0과 b를 삭제해서 이진수만 보이게 설정
    if num >= 0:
        asd.pop(0)
        asd.pop(0)

    # 이진수 1이 나오는 경우 딸기가 들어가게, 0이 들어가는 경우 V가 들어가게 설정
        sdf=[]
        for i in range(len(asd)):
            if asd[i] == '1':
                sdf.append('딸기')
            elif asd[i] == '0':
                sdf.append('V')
    # 총 4글자가 되어야 하는데 만약 글자수가 비는 경우 앞에 V가 들어가게 각각 설정
        if len(sdf) == 1:
            print('VVV' + sdf[0])
        elif len(sdf) == 2:
            print('VV' + sdf[0]+sdf[1])
        elif len(sdf) == 3:
            print('V' + sdf[0]+sdf[1]+sdf[2])
        else:
            for i in sdf:
                print(i,end='')
            print()























