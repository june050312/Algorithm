import sys

input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]
        
def boardCheck():
    rowCnt = [[1 for _ in range(n)] for _ in range(n)]
    colCnt = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        # row count
        c = 0
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                rowCnt[i][c] += 1
            else:
                c += 1
        rowCnt[i] = max(rowCnt[i])

        # colum count
        c = 0
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                colCnt[i][c] += 1
            else:
                c += 1
        colCnt[i] = max(colCnt[i])

    return max(max(rowCnt), max(colCnt))

def rowSwap(i, j):
    temp = board[i][j]
    board[i][j] = board[i][j + 1]
    board[i][j + 1] = temp

def colSwap(i, j):
    temp = board[i][j]
    board[i][j] = board[i + 1][j]
    board[i + 1][j] = temp

ans = 1
for i in range(n):
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            rowSwap(i, j)
            ans = max(ans, boardCheck())
            rowSwap(i, j)

    for j in range(n - 1):
        if board[j][i] != board[j + 1][i]:
            colSwap(j, i)
            ans = max(ans, boardCheck())
            colSwap(j, i)

print(ans)