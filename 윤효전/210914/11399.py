import itertools
from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
S = sorted(map(int, input().split()))
S = itertools.accumulate(S, lambda a, b: a+b)
print(sum(S))
