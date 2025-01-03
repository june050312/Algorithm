import sys

input = sys.stdin.readline

while 1:
    try:
        n = int(input())

        remainder = 1
        length = 1
        while remainder % n != 0:
            remainder = (remainder * 10 + 1) % n
            length += 1
        print(length)
    except:
        break