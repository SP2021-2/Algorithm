import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

mage =[]
for _ in range(N):
    mage.append(list(map(int, list(sys.stdin.readline().rstrip()))))

def pprint(arr):
    for line in arr:
        print(line)

pprint(mage)

def bfs():
    q = deque([(0,0,1)])
    visited = [(0,0)]
    
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]

    cnt = 0
    # 코드 작성 하기


print(bfs())