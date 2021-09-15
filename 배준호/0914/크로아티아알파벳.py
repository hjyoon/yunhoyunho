import sys
sys.stdin = open('input.txt')

def alpha(word):
    global cnt
    for i in range(len(word)):
        if word[i] == 'c':
            if word[i+1] == '=' or '-':
                cnt += 1
            else:
                return
        elif word[i] == 'd':
            if word[i+1] == 'z':
                if word[i+2] == '=':
                    cnt += 1
            elif word[i+1] == '-':
                cnt += 1
            else:
                return
        elif word[i] == 'l':
            if word[i+1] == 'j':
                cnt += 1
            else:
                return
        elif word[i] == 'n':
            if word[i+1] == 'j':
                cnt += 1
            else:
                return
        elif word[i] == 's':
            if word[i+1] == '=':
                cnt += 1
            else:
                return
        elif word[i] == 'z':
            if word[i+1] == '=':
                cnt += 1
            else:
                return
    return cnt

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = list(input())

cnt = 0

print(alpha(word))
