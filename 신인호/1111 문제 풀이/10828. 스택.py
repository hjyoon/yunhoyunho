from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


class Stack:
    def __init__(self, N):
        self.N = N
        self.arr = [0] * N
        self.rear = -1
    
    def push(self, x):
        if self.rear < self.N:
            self.rear += 1
            self.arr[self.rear] = x
    
    def pop(self):
        top = self.top()
        if top > -1:
            self.rear -= 1
        return top

    def size(self):
        return self.rear + 1
    
    def empty(self):
        return 1 if self.rear == -1 else 0
    
    def top(self):
        if self.rear >= 0:
            return self.arr[self.rear]
        else:
            return -1


N = int(input())
stack = Stack(N)

for _ in range(N):
    command, *arg = input().split()
    if arg:
        stack.push(int(arg[0]))
    else:
        # 클래스 내 메서드를 문자열 형태로 받아 실행하는 법
        # https://www.kite.com/python/answers/how-to-call-a-function-by-its-name-as-a-string-in-python
        method = getattr(stack, command)
        print(method())
