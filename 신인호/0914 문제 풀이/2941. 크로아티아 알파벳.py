from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


CROATIAN = set([
    'c=', 
    'c-', 
    'dz=', 
    'd-', 
    'lj', 
    'nj', 
    's=', 
    'z='
    ])


def count_char(word):
    char_count = 0

    # 첫 번째 글자부터 마지막 글자까지 순회
    i = 0
    while i < len(word):
        # 현재부터 세 글자가 크로아티안 알파벳이면
        # 알파벳 하나로 인식.
        # -> 현재 위치를 세 칸 뒤로 이동
        if word[i:i+3] in CROATIAN:
            i += 3
        elif word[i:i+2] in CROATIAN:
            i += 2
        # 크로아티안 알파벳 목록에 없으면 그냥 알파벳
        else:
            i += 1
        # 알파벳 개수 1 증가
        char_count += 1
    
    return char_count


for word in sys.stdin:
    print(count_char(word.strip()))