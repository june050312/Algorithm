import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    for num in map(int, input().split()):
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
                
print(heap[0])