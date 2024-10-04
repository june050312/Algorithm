def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return True
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)
    
import sys
from collections import deque
n = int(sys.stdin.readline())
nNum = list(map(int, sys.stdin.readline().strip().split()))
nNum.sort()
m = int(sys.stdin.readline())
mNum = list(map(int, sys.stdin.readline().strip().split()))
result = deque()
for i in mNum:
    if binary_search(nNum, i, 0, n - 1):
        result.append(1)
    else:
        result.append(0)
print(*result)