from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


class Queue:
    def __init__(self, N):
        self.N = N
        self.arr = [0] * N
        self.first = -1
        self.rear = -1
    
    def push(self, x):
        if self.rear < self.N:
            self.rear += 1
            self.arr[self.rear] = x
    
    def pop(self):
        front_value = self.front()
        if front_value > -1:
            self.first += 1
        return front_value

    def size(self):
        return self.rear - self.first
    
    def empty(self):
        return 1 if self.rear == self.first else 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.first + 1]
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.rear]


N = int(input())
queue = Queue(N)

for _ in range(N):
    command, *arg = input().split()
    if arg:
        queue.push(int(arg[0]))
    else:
        # 클래스 내 메서드를 문자열 형태로 받아 실행하는 법
        # https://www.kite.com/python/answers/how-to-call-a-function-by-its-name-as-a-string-in-python
        method = getattr(queue, command)
        print(method())
