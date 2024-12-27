import sys

input = sys.stdin.readline

def getPrimeList(end):
    primeList = [i for i in range(end + 1)]

    primeList[0] = primeList[1] = 0

    for i in range(2, int(end ** (1/2)) + 1):
        if primeList[i]:
            for j in range(i * i, end + 1, i):
                primeList[j] = 0

    return primeList

primeList = getPrimeList(1000000)

while 1:
    targetNum = int(input())

    if targetNum == 0:
        break
    
    for i in range(3, targetNum // 2 + 1, 2):
        if primeList[i] and primeList[targetNum - i]:
            print(f"{targetNum} = {i} + {targetNum - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")