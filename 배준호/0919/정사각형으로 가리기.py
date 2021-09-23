import sys
sys.stdin = open('input.txt')


N = int(input())
A = []
B = []
Z = []
R = []
for i in range(N):
    X, Y = map(int, input().split())
    A += [X]
    B += [Y]
    R += [(X, Y)]
if (max(A)-min(A)) == (max(B)-min(B)):
    for i in range(min(A), max(A)+1):
        Z += [(i, min(B))]
        Z += [(i, max(B))]
    for i in range(min(B), max(B)+1):
        Z += [(min(A), i)]
        Z += [(max(A), i)]
else:
    if (max(A) - min(A)) >= (max(B) - min(B)):
        for i in range(min(A), max(A) + 1):
            Z += [(i, min(B))]
            Z += [(i, max(B))]
        for i in range(min(B), min(B) + max(A)-min(A)):
            Z += [(min(A), i)]
            Z += [(max(A), i)]
    else:
        for i in range(min(A), max(A) + max(B)-min(B)):
            Z += [(i, min(B))]
            Z += [(i, max(B))]
        for i in range(min(B), max(B) + 1):
            Z += [(min(A), i)]
            Z += [(max(A), i)]
a = 0
for i in range(len(R)):
    if R[i] in Z:
        a = max((max(B)-min(B)), max(A)-min(A))
    else:
        a = -1
        break

print(a)