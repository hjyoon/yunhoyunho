from pprint import pprint
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
ans = 0
st = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        st.append(tmp)
    if st:
        st[-1][-1] -= 1
        if st[-1][-1] == 0:
            ans += st[-1][-2]
            st.pop()

print(ans)
