import sys

input = sys.stdin.readline

board = [[0 for _ in range(1001)] for _ in range(1001)]
n = int(input())
for k in range(n):
    x, y, w, h = map(int, input().split())
    for i in range(h):
        board[y + i][x : x + w] = [k + 1] * w

for i in range(n):
    cnt = 0
    for j in board:
        cnt += j.count(i + 1)
    print(cnt)