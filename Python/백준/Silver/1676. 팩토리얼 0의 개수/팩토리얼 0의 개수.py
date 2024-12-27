import sys, math

a = list(str(math.factorial(int(sys.stdin.readline().strip()))))
cnt = 0
for i in range(len(a)):
    if a.pop() == '0':
        cnt += 1
    else:
        print(cnt)
        break