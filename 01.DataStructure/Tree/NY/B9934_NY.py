#백준 - 완전 이진 트리 9934

import sys

k = int(input())
numOrder = sys.stdin.readline().split()

bt = []
for i in range (k) :
    bt.append([])

#재귀함수
def binaryArr (arr, lev) :
    if len(arr) == 1 :
        bt[lev].append(arr[0])
        return bt
    else :
        #배열의 중간을 뽑아냄
        middle = len(arr) // 2
        bt[lev].append(arr[middle])
        
        # 배열을 반으로 나눔
        binaryArr(arr[0 : middle], lev+1)
        binaryArr(arr[middle+1 : ], lev+1)

binaryArr(numOrder, 0)

for i in range (k) :
    print(*bt[i])

