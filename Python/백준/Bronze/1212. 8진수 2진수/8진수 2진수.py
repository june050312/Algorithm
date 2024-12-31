import sys

print(format(int('0o' + sys.stdin.readline().strip(), 8), 'b'))