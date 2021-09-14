from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


S = input().rstrip()
ans = S.replace('c=', '.').replace('c-', '.').replace('dz=',
                                                      '.').replace('d-', '.').replace('lj', '.').replace('nj', '.').replace('s=', '.').replace('z=', '.')
print(len(ans))
