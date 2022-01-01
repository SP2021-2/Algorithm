# b1260
import sys
from collections import deque

def DFS(v):
    visit_D[v] = 1
    print(v, end = " ")
    for i in range(1, n + 1):
        if visit_D[i] == 0 and graph[v][i] == 1 :
            DFS(i)

def BFS(v):
    q = deque()
    q.append(v)
    visit_B[v] = 1
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            if visit_B[i] == 0 and graph[v][i] == 1 :
                q.append(i)
                visit_B[i] = 1

n, m, v = map(int, sys.stdin.readline().split())

graph = []
visit_D = [0] * (n + 1)
visit_B = [0] * (n + 1)

for _ in range(n + 1) :
    graph.append([0] * (n + 1)) 
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

DFS(v)
print()
BFS(v)
