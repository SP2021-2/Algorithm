def pprint(arr):
    for line in arr:
        print(line)
# 5 7
# 0 1 1
# 0 2 3
# 1 2 3
# 1 3 6
# 2 3 4
# 2 4 2
# 3 4 5

import sys
import heapq as hq
N, M = map(int, sys.stdin.readline().split(" "))
W = [[float('inf')] * N for _ in range(N)]

h = []
for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split(" "))
    hq.heappush(h, (w, i, j))

print(h)
def Kruskal(heap, source):
    answer = []
    visited = []
    while heap:
        w, i, j = hq.heappop(heap)

    return answer

print(Kruskal(h, 0))