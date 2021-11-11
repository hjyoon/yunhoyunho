from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
괄호 -> 스택
"""

stack = [0] * 100
pair = {')': '(', ']': '['}

while True:
    # 문자열 입력받고, .이면 종료
    string = input().rstrip()
    if string == '.':
        break

    # 문자열 쭉 검색
    idx = 0
    for char in string:
        # 여는 괄호면 스택에 추가
        if char == '(' or char == '[':
            stack[idx] = char
            idx += 1
        # 닫는 괄호일 때
        elif char == ')' or char == ']':
            # 스택이 비어있으면 X
            if idx < 0:
                print('no')
                break
            # 마지막과 달라도 X
            elif stack[idx - 1] != pair[char]:
                print('no')
                break
            # 같을 때만 스택에서 pop
            else:
                idx -= 1
    else:
        # FIXME: 여는 괄호만 있는 경우도 추가해야 함
        if idx != 0:
            print('no')
        else:
            print('yes')
