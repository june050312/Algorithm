import sys

input = sys.stdin.readline

prog_range, target_num = map(int, input().split())
prog = list(map(int, input().split()))

count = 0
cur_num = 0
rear = 0
for front in range(prog_range):
    cur_num += prog[front]
    while cur_num > target_num and rear < front:
        cur_num -= prog[rear]
        rear += 1
    if cur_num == target_num:
        count += 1

print(count)