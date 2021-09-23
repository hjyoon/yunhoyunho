word = input().upper()

C = [0]*123
for i in range(len(word)):
    C[ord(word[i])] += 1


man = []
for j in range(len(C)):
    if C[j] == max(C):
        man.append(j)
if len(man) >= 2:
    print('?')
else:
    print(chr(man[0]))