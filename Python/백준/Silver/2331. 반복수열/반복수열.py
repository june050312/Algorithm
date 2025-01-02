import sys
input = sys.stdin.readline

A, P = map(int, input().strip().split())
Q = []

Q.append(A)

i = 1
cnt = 0
while 1:
    num = list(map(int, str(Q[i - 1])))
    num = sum(map(lambda x : x ** P, num))

    if num in Q:
        while Q.pop(0) != num:
            cnt += 1
        break

    Q.append(num)
    i += 1

print(cnt)