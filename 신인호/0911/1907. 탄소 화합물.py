# 1. 화학식에서 원소 개수를 세서 딕셔너리 만들기
def count_dict(exp):
    dict = {}
    for char in exp:
        # 원소인 경우
        if char in ['C', 'H', 'O']:
            element = char
            # 일단 한 개 넣음
            dict[element] = dict.get(element, 0) + 1
        # 숫자인 경우
        else:
            # 뒤에 숫자가 오면 그대로 넣고,
            # 아까 한 개 넣어줬으니, 한 개 뺌
            dict[element] += int(char) - 1
    return dict


# 2. 없는 원소의 개수는 0으로 초기화
def complement_empty_key(left, middle, right):
    for elem in right.keys():
        if elem not in left:
            left[elem] = 0
        if elem not in middle:
            middle[elem] = 0


# 3. 조건 일치하는 걸 찾기 위해 무지성 검색
def brute_force_sum(left, middle, right):
    # 계수는 1부터 10까지므로, 이게 범위가 됨.
    # (1, 1, 1) 부터 (10, 10, 10)까지 찾아 봄
    for x in range(1, 11):
        for y in range(1, 11):
            for z in range(1, 11):
                # 각각의 원자들에 대해
                for elem in right.keys():
                    # 원자의 개수를 구함
                    a = left[elem]
                    b = middle[elem]
                    c = right[elem]
                    # (원자 개수 * 분자 계수)의 합이 같은지 확인
                    if a * x + b * y != c * z:
                        # 같지 않으면 다음 원소 검색
                        break
                # break 없던 경우 = 조건 일치 -> 결과 반환
                else:
                    return x, y, z


# '=' 기호를 '+'로 바꾸고, 
# '+'를 구분자로 나누면 리스트 세 개로 나눠짐
exps = input().replace('=', '+').split('+')

# 각 분자식마다 {원소: 원소 개수}의 딕셔너리를 구함
left = count_dict(exps[0])
middle = count_dict(exps[1])
right = count_dict(exps[2])

# 없는 원소의 개수는 0으로 초기화
complement_empty_key(left, middle, right)

# 브루트포스 방식으로 계수를 찾아냄
x, y, z = brute_force_sum(left, middle, right)
print(x, y, z)