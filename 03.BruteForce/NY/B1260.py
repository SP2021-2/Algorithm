#백준 1260 - DFS, BFS
# 왜 자꾸... check를 못 찾는다고 하는 거지..?

from collections import deque

N, M, V = map(int, input().split())

check = [False for _ in range(N+1)]
G = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range (M) :
    x, y = list(map(int, input().split()))
    G[x][y] = G[y][x] = 1



def DFS (v) :
    print(v, " ")
    check[v] = True

    for i in range (1, N+1) :
        if G[v][i] == 1 & check[i] :
            check = DFS(i)
        

def BFS (v) :
    gQueue = deque()
    gQueue.append(v)
    check[v] = True

    while len(gQueue) != 0 :
        v = gQueue.popleft()
        print(v, " ")

        for i in range(1, N+1) :
            if G[v][i] == 1 & check[i] :
                gQueue.append(i)
                check[i] = True


DFS(V)
check = [False for _ in range(N+1)]
BFS(V)