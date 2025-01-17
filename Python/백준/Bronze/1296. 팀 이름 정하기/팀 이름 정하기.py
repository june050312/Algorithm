import sys

input = sys.stdin.readline

nameCnt = [0, 0, 0, 0]

for i in input().strip():
    if i == "L":
        nameCnt[0] += 1
    elif i == "O":
        nameCnt[1] += 1
    elif i == "V":
        nameCnt[2] += 1
    elif i == "E":
        nameCnt[3] += 1

teamCnt = {}
for _ in range(int(input())):
    L = nameCnt[0]
    O = nameCnt[1]
    V = nameCnt[2]
    E = nameCnt[3]

    teamName = input().strip()
    for i in teamName:
        if i == "L":
            L += 1
        elif i == "O":
            O += 1
        elif i == "V":
            V += 1
        elif i == "E":
            E += 1

    teamCnt[(teamName)] = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

ans = dict(sorted(teamCnt.items()))
print(max(ans, key = ans.get))