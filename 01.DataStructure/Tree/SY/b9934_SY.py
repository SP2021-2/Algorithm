# b9934_SY
import heapq
k = int(input())
buildings = [int(x) for x in input().split()]
heap = []


def cutting(buildings, n):
    mid = int(len(buildings)/2)
    left_buildings = []
    right_buildings = []
    if mid > 0:
        left_buildings = buildings[:mid]
        right_buildings = buildings[mid+1:]
        heapq.heappush(heap, (n, buildings[mid]))  # (우선 순위, 값)
        n = n + 1
        cutting(left_buildings, 2*n+1)  # 홀수 index 에 차례대로 넣음
        cutting(right_buildings, 2*(n+1))  # 짝수 index 에 차례대로 넣음
    else:
        heapq.heappush(heap, (n, buildings[0]))


def printq(heap, m):
    for i in range(2**m):
        print(heapq.heappop(heap)[1], end=" ")  # index 1 == value


cutting(buildings, 0)

for m in range(k):
    printq(heap, m)
    print()
