import sys
for i in list(sys.stdin.readline().rstrip()):
    if 'A' <= i <= 'M' or 'a' <= i <= 'm':
        print(chr(ord(i) + 13), end='')
    elif 'N' <= i <= 'Z':
        print(chr(65 + ord(i) - 78), end='')
    elif 'n' <= i <= 'z':
        print(chr(97 + ord(i) - 110), end='')
    else:
        print(i, end='')
print()