import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline

X, Y = map(int, input().split())

month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

total = 0
for i in range(1, X):
    total += month[i]
total += Y

print(day[total % 7])
