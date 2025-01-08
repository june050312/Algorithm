import sys

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

'''
I 미노, O 미노, L 미노, S 미노, T 미노 회전, 대칭 다 구현해놓고
합 저장한 다음에 max 써서 구하면 될 듯?
'''

def getFirstI(i, j):
    return paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]

def getSecondI(i, j):
    return paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]

def getO(i, j):
    return paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1]

def getFirstL(i, j):
    return paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]

def getSecondL(i, j):
    return paper[i+1][j] + paper[i][j] + paper[i][j+1] + paper[i][j+2]

def getThirdL(i, j):
    return paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]

def getFourthL(i, j):
    return paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2] + paper[i][j+2]

def getFirstJ(i, j):
    return paper[i+2][j] + paper[i+2][j+1] + paper[i+1][j+1] + paper[i][j+1]

def getSecondJ(i, j):
    return paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]

def getThirdJ(i, j):
    return paper[i+2][j] + paper[i+1][j] + paper[i][j] + paper[i][j+1]

def getFourthJ(i, j):
    return paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]

def getFirstZ(i, j):
    return paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j] + paper[i+2][j]

def getSecondZ(i, j):
    return paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2]

def getFirstS(i, j):
    return paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]

def getSecondS(i, j):
    return paper[i+1][j] + paper[i+1][j+1] + paper[i][j+1] + paper[i][j+2]

def getFirstT(i, j):
    return paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1]

def getSecondT(i, j):
    return paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]

def getThirdT(i, j):
    return paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]

def getFourthT(i, j):
    return paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1]

minos = [
    getFirstI, 
    getSecondI, 
    getO, 
    getFirstL, 
    getSecondL, 
    getThirdL, 
    getFourthL, 
    getFirstJ, 
    getSecondJ,
    getThirdJ,
    getFourthJ,
    getFirstS,
    getSecondS,
    getFirstZ,
    getSecondZ,
    getFirstT,
    getSecondT,
    getThirdT,
    getFourthT
]

ans = []

for mino in minos:
    for i in range(n):
        for j in range(m):
            try:
                ans.append(mino(i, j))
            except:
                break

print(max(ans))