#백준 - 최대 힙 11279

import heapq
import sys


N = int(input())

maxHeap = []

for n in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(maxHeap) != 0 :
            print(-heapq.heappop(maxHeap))
        else : print(0)
    else :
        heapq.heappush(maxHeap, -x)

# heapq 말고, 직접 구현하는 거도 꼭 다시 해보기
# def append_sort (x) :
#     maxHeap.append(x)

#     present = maxHeap.index(x)
#     parent = (present-1) // 2
#     print(present, parent)

#     if len(maxHeap) > 1 :
#         while maxHeap[parent] < maxHeap[present] :
#             maxHeap.insert(present, maxHeap.pop(parent))
#             maxHeap.insert(parent, maxHeap.pop(present + 1))

#             present = parent
#             parent = (present-1) // 2

#     print(maxHeap)

# def pop_sort(index) :
#     maxHeap.insert(0, -1)

#     present = index
#     child_L = present + 1
#     child_R = present + 2

#     while maxHeap.index(-1) != len(maxHeap) :
#         if maxHeap[child_L] > maxHeap[child_R] :
#             maxHeap.insert(0, maxHeap[child_L])
#             maxHeap.pop(child_L+1)
#         elif maxHeap[child_L] < maxHeap[child_R] :
#             maxHeap.insert(0, maxHeap[child_R])
#             maxHeap.pop(child_R+1)

#         child_L = maxHeap.index(-1) * 2 + 1
#         child_R = maxHeap.index(-1) * 2 + 2
    
#     maxHeap.remove(-1)
#     print(maxHeap)




# for n in range(N) :
#     x = int(input())

#     if x == 0 :
#         try : 
#             print("print", maxHeap.pop(0))
#             if len(maxHeap) > 1 :
#                 pop_sort(0)
#         except(IndexError) : print("print", 0)

#     else :
#         append_sort(x)

