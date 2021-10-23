from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

# 실패한 방법
"""
사전순 앞서는 것 => 사전순 정렬 필요
1) 홀수인 경우엔 ㄱㄱㅁㅁㅈㅈㅇ 와 같은 식으로,
2) 짝수인 경우엔 ㄱㄱㅁㅁㅈㅈ 처럼 정렬

팰린드롬 => 두 개씩 짝지어지는 것

정렬 후 2개씩 끊어서, 
각각 처음과 맨 끝에 놓고, 
한 칸씩 당겨오는 식으로 하면 
팰린드롬 완성! (ㄱㄴㄷㄷㄴㄱ)

홀수인 경우엔 한 개만 남아야 함

FIXME: AABCC처럼 더 빠른 게 홀수 개(하나)인 경우도 있음...
=> 처음 만나는 건 따로 빼놨다가 나중에 중간에 넣기.
그러나 또 그런 게 있다면 팰린드롬은 성립 불가.
"""

IMPOSSIBLE_MSG = "I'm Sorry Hansoo"

def palindrome_by_pairs(string):
    # 문자열 정렬한 리스트 생성
    chars = sorted(list(string))
     
    # 결과를 담을 빈 리스트 생성
    length = len(chars)
    palindrome = [''] * length

    # 홀수인 경우 때 쓸 변수들
    odd_encountered = False
    odd_char = ''

    # 처음부터 끝까지, 2개씩 짝지어 가져오기
    i = 0
    while i + 1 < length:
        left = chars[i]
        right = chars[i + 1]

        # 서로 다르면 홀수인 경우임.
        if left != right:
            # 처음인 경우에만 따로 저장. 
            if not odd_encountered:
                odd_char = left
                odd_encountered = True
                # 한 칸만 전진해야 다음부터 2개씩 짝지어짐.
                i += 1
                continue
            # 또 그런 게 있으면 팰린드롬 X
            else:
                return IMPOSSIBLE_MSG
        
        # 서로 같으면 빈 배열 양쪽 끝에 넣기
        else:
            palindrome[i] = left
            palindrome[length - 1 - i] = right
    
        # 두 칸씩 전진.
        i += 2

    # 홀수인 경우엔, 마지막 것을 중간에 넣기
    if length % 2:
        palindrome[length // 2] = odd_char
    
    return ''.join(palindrome)

print(palindrome_by_pairs(input()))
