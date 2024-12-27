from string import ascii_lowercase, ascii_uppercase
a = list(ascii_lowercase)
A = list(ascii_uppercase)
cnt = [0,0,0,0]
while True:
    try:
        for i in list(input()):
            if i in a:
                cnt[0] += 1
            elif i in A:
                cnt[1] += 1
            elif i == ' ':
                cnt[3] += 1
            else:
                cnt[2] += 1
        print(*cnt)
        cnt = [0,0,0,0]
    except:
        break