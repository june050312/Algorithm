import sys
from collections import deque
input = sys.stdin.readline

def bfs(box):
    q = deque()
    unripe = 0

    for i in range(z):
        for j in range(y):
            for k in range(x):
                if box[i][j][k] == 1:
                    q.append([k, j, i])
                elif box[i][j][k] == 0:
                    unripe += 1

    move = [
        [0, 0, 0],
        [-1, 0, 0], [1, 0, 0],
        [0, -1, 0], [0, 1, 0],
        [0, 0, -1], [0, 0, 1]
    ]

    while q:
        cx, cy, cz = q.popleft()
        
        for mx, my, mz in move:
            nx, ny, nz = cx + mx, cy + my, cz + mz

            if 0 <= nx < x and 0 <= ny < y and 0 <= nz < z and box[nz][ny][nx] == 0:
                q.append([nx, ny, nz])
                box[nz][ny][nx] = box[cz][cy][cx] + 1
                unripe -= 1

    if unripe == 0:
        return box[cz][cy][cx] - 1
    else:
        return -1
                
x, y, z = map(int, input().strip().split())
box = []
for i in range(z):
    box.append([])
    for j in range(y):
        box[i].append(list(map(int, input().strip().split())))


result = bfs(box)

print(result)