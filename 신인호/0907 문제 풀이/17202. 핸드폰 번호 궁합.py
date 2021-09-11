from collections import deque


# 두 수를 번갈아가며 만든 리스트
def alternating_list(num_a, num_b):
    result = []
    for i in range(len(num_a)):
        result.append(num_a[i])
        result.append(num_b[i])
    return result


# 번갈아가며 만든 리스트를, 인접 숫자끼리 더해가며 합을 구함
def alternating_sum(alt_list):
    # 큐를 이용
    result = deque(alt_list)
    # 마지막에 남는 숫자가 2개일 때까지 반복
    while len(result) > 2:
        for i in range(len(result) - 1):
            # 인접 숫자끼리의 합의 일의 자리
            new_digit = (result[0] + result[1]) % 10
            # 이 숫자를 맨 뒤에 추가
            result.append(new_digit)
            # 앞 숫자는 버리고, 뒷 숫자는 다음 기준이 됨
            result.popleft()
        # 원래 리스트에서 맨 뒤에 있던 숫자를 버림
        # -> 새로 만든 숫자들만 남음
        result.popleft()
    return result


a = list(map(int, list(input())))
b = list(map(int, list(input())))
alt_list = alternating_list(a, b)
alt_sum = alternating_sum(alt_list)
print(*alt_sum, sep='')