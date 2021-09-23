# 총 길이가 홀수? 가운데 뺀 애들 같은지?
# 짝수면 걍 양옆


while True:
    try:
        word = input()
        if word == '0':
            break
        while True:
            if word[0] == word[-1]:
                word = word[1:-1]
                # if word[0] != word[-1]:
                #     print('no')
                #     break
            if len(word) == 1 or len(word) == 0:
                print('yes')
                break

            if word[0] != word[-1]:
                print('no')
                break

    except:
        break

