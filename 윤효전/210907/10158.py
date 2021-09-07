from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

W, H = map(int, input().split())
x, y = map(int, input().split())

t = int(input())

y_list = list(range(H+1)) + list(range(1, H))[::-1]
x_list = list(range(W+1)) + list(range(1, W))[::-1]

tmpx = (x+t) % (W*2)
tmpy = (y+t) % (H*2)

print(x_list[tmpx], y_list[tmpy])
