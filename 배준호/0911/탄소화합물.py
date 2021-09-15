import sys
sys.stdin = open('input.txt')

arr = list(input())
stack = []
calculate = []

for i in range(len(arr)):
    if arr[i] == 'C' or arr[i] == 'H' or arr[i] == 'O':
        if arr[i+1]:
        stack += arr[i]
    elif arr[i] == '+' or arr[i] == '=':
        calculate += arr[i]
    else:
        stack += stack.pop() * int(arr[i])

    print(stack)
