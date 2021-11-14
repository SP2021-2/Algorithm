# b11279_SY
import sys
import heapq
heap = []
N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) >= 1:
            print(-heapq.heappop(heap))  # index 1
        else:
            print(0)
    elif x > 0:
        heapq.heappush(heap, -x)  # 부호를 변경하여 힙에 삽입
