import itertools
import sys
sys.stdin = open('input.txt')

def function(A, B):
    global cnt
    for j in range(7):
        for k in range(5):
            if A[j][k] == B[j][k]:
                count[i] += 1
            else:
                return
    return cnt



N = int(input())
blank = []
count = [0] * N
print(count)
for i in range(N):
    arr = [list(input()) for _ in range(5)]
    blank.append(arr)

print(blank)
# for i in range(N):


#
comb = itertools.combinations(blank, 2)
print(list(comb))
for i in range(N):
    function(list(comb)[i])