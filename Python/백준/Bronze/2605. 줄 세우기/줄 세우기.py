import sys

input = sys.stdin.readline

numOfStudent = int(input())
cards = list(map(int, input().split()))

line = [i for i in range(1, numOfStudent + 1)]
for i in range(1, numOfStudent):
    student = line.pop(i)
    line.insert(i - cards[i], student)

print(*line)