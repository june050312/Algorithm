import sys

input = sys.stdin.readline

oper_num = int(input())

S = set()
for _ in range(oper_num):
    comm = input().strip()
    num = 0
    if comm == "all" or comm == "empty":
        if comm == "all":
            for i in range(20):
                S.add(i + 1)
        else:
            S = set()
    else:
        comm, num = comm.split()
        num = int(num)

        if comm == "add":
            S.add(num)
        elif comm == "remove":
            if num in S:
                S.remove(num)
        elif comm == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif comm == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)