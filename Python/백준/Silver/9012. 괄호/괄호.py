import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    cnt, check = 0, 0
    temp = list(sys.stdin.readline().strip())
    for i in temp:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            check += 1
    if cnt == 0 and check == 0:
        print('YES')
    else:
        print('NO')