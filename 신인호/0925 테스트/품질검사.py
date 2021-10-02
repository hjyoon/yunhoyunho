"""
1. 결과가 합격일 때 -> 모든 부품 정상
2. 결과가 불합 & 정상 부품 두 개 -> ?를 X로
3. 결과가 불합 & 정상 부품 한 개 -> ?를 ?로 => 스킵
"""

PASS = 1
BROKEN = 0
NORMAL = 1
UNKNOWN = 2


# 개수를 입력받아 그만큼의 부품 배열을 만듦
# 이때 번호를 그대로 쓰기 위해 배열 크기를 1 더 늘림.
A, B, C = map(int, input().split())
components = [2] * (A + B + C + 1)

N = int(input())
tests = []
for _ in range(N):
    test = list(map(int, input().split()))
    if test[3] == PASS:
        # 검사 결과 합격 -> 부품들에 정상 표시하고 넘김
        for i in range(3):
            components[test[i]] = NORMAL
    else:    
        # 불합격 -> 검사 결과에 넣음
        tests.append(test)

for test in tests:
    # 각 부품들의 상태를 조사
    normal_list = []
    unknown_list = []
    for i in range(3):
        if components[test[i]] == NORMAL:
            normal_list.append(test[i])
        elif components[test[i]] == UNKNOWN:
            unknown_list.append(test[i])
    
    # 검사 결과가 실패인데 정상인 부품이 2개인 경우, 
    # 나머지 한 개는 무조건 X
    if len(normal_list) == 2:
        x = unknown_list[0]
        components[x] = BROKEN

print(*components[1:], sep='\n')
