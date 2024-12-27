import sys
from string import ascii_uppercase
n = int(sys.stdin.readline())
a = list(map(str, sys.stdin.readline().strip()))
m = [float(sys.stdin.readline()) for _ in range(n)]
myDict = {}
num = []
for i in range(n):
    myDict[ascii_uppercase[i]] = m[i]
for i in a:
    if 'A' <= i <= 'Z':
        num.append(myDict[i])
    else:
        str2 = num.pop()		# num 리스트의 마지막 2항목을 꺼내와서 계산한다.
        str1 = num.pop()

        if i =='+' :
            num.append(str1+str2)
        elif i == '-' :
            num.append(str1-str2)
        elif i == '*' :
            num.append(str1*str2)
        elif i == '/' :
            num.append(str1/str2)
print("%.2f" % num[0])