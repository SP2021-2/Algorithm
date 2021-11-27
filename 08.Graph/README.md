# 그래프 (Graph)
그래프는 정점(vertex)과 간선(edge)으로 구성된 한정된 자료구조를 의미한다. 컴퓨터 시스템에 그래프를 저장하는 방법은 여러가지가 있는데, 실제 적용에 있어서 최적의 자료구조는 리스트와 행렬로 구별된다. 리스트는 적은 메모리 공간을 요구한다. 행렬은 많은 양의 메모리를 필요로 하지만 더욱 빠른 접근이 가능하다.

__정점의 개수가 V개 간선의 개수가 E개인 그래프에 대해__
- 간선리스트 : E*2 or E*3 이차원 배열에 간선 정보 저장
- 인접행렬 : V*V 이차원 배열에 그래프 정보를 저장
- 인접리스트 : V개의 연결리스트에 그래프 정보를 저장
### 그래프 용어
- 무향간선, 유향간선, 다중간선
- 인접, 부속 : 간선e는 정점 v1, v2에 부속한다., 차수 : 정점에 부속된 간선의 수
- Cycle : 시작정점과 끝 정점이 같은 경로
- 무향그래프, 유향그래프, 가중치그래프, 정규그래프, 완전그래프, 연결그래프, 부분그래프, 트리그래프

## 쾨니히스베르크 다리 건너기 문제 
<image src="./images/오일러 스케치.png">

> 쾨니히스베르크시의 한 가운데는 프레겔 강이 흐르고 있고 여기에는 가운데 섬들과 연결되어있는 일곱 개의 다리가 있다. 그 다리들을 한 번씩만 차례로 모두 건널 수 있겠는가?

## 외판원 문제(The Travleing sales-woman problem) - DP
<image src="./images/외판원문제.png">
: 외판원이 거주하고 있는 도시에서 출발하여 n개의 각 도시를 한 번씩 방문하고, 다시 출발한 도시로 돌아오는 가장 짧은 여행길을 찾고 싶다. 이런 최단 여행 경로를 구하는 문제를 외판원 문제라고 한다.

만약 도시가 20개라고 할 때, 이 문제의 정답을 찾기 위해 다녀야 하는 총 경로의 수는 20!다. `2,432,902,0008,176,640,000`이다.

1. 동적계획으로 풀기
- W : 주어진 그래프의 인접행렬
- V : 모든 도시의 집합
- A : V의 부분집합
- D[vi][A]: A에 속한 도시를 각각 한 번씩만 거쳐서 vi에서 v1으로 가는 최단 경로의 길이

__재귀 관계식__
```
D[vi][A] = minimum(W[i][j]+ D[vj][A-vj])
D[vi][{}] = W[i][1]
```

- 부분집합 표현 : 비트를 이용한 부분집합의 표현과 연산
V - {v1} = {v2, v3, v4}
0 ~ 7 까지 표현 가능
0 - {}
1 - {v2}
2 - {v3}
4 - {v4}
3 - {v2, v3}
5 - {v2, v4}
6 - {v3, v4}
7 - {v2, v3, v4}

```
def travel (W):
    n = len(W) - 1
    size = 2 ** (n - 1)
    D = [[0] * size for _ in range(n + 1)]
    P = [[0] * size for _ in range(n + 1)]
    for i in range(2, n + 1):
        D[i][0] = W[i][1]
    for k in range(1, n - 1):
        for A in range(1, size):
            if (count(A, n) == k):
                for i in range(2, n + 1):
                    if (not isIn(i, A)):
                        D[i][A], P[i][A] = minimum(W, D, i, A)
    A = size - 1
    D[1][A], P[1][A] = minimum(W, D, 1, A)
    return D, P

def minimum (W, D, i, A):
    minValue = INF
    minJ = 1
    n = len(W) - 1
    for j in range(2, n + 1):
        if (isIn(j, A)):
            m = W[i][j] + D[j][diff(A, j)]
            if (minValue > m):
                minValue = m
                minJ = j
    return minValue, minJ
```

2. 분기 한정으로 풀기
```
def travel2 (W):
    global minlength, opttour
    n = len(W) - 1
    PQ = PriorityQueue()
    v = SSTNode(0)
    v.path = [1]
    v.bound = bound(v, W)
    minlength = INF
    PQ.put((v.bound, v))
    while (not PQ.empty()):
        v = PQ.get()[1]
        if (v.bound < minlength):
            for i in range(2, n + 1):
                if (v.contains(i)): 
                    continue
                u = SSTNode(v.level + 1)
                u.path = v.path[:]
                u.path.append(i)
                if (u.level == n - 2):
                    for k in range(2, n + 1):
                        if (not u.contains(k)):
                            u.path.append(k)
                    u.path.append(1)
                    if (length(u.path, W) < minlength):
                        minlength = length(u.path, W)
                        opttour = u.path[:]
                else:
                    u.bound = bound(u, W)
                    if (u.bound < minlength):
                        PQ.put((u.bound, u))

def bound(v, W):
    n = len(W) - 1
    total = length(v.path, W)
    for i in range(1, n + 1):
        if (hasOutgoing(i, v.path)):
            continue
        min = INF
        for j in range(1, n + 1):
            if (i == j): continue
            if (hasIncoming(j, v.path)): continue
            if (j == 1 and i == v.path[len(v.path) - 1]): continue
            if (min > W[i][j]): min = W[i][j]
        total += min
    return total
```

## 최단 경로 문제
: 가중 그래프에서 간선의 가중치의 합이 최소가 되는 경로를 찾는 문제

- BFS : 가중치가 없거나 모든 가중치가 동일한 그래프에서 최단경로를 구하는 경우
- 다익스트라 알고리즘 : 음이 아닌 가중 그래프에서의 단일 쌍, 단일 출발, 단일 도착 최단 경로 문제
- 벨만-포드 알고리즘 : 가중그래프에서의 단일 쌍, 단일 출발, 단일 도착 최단 경로 문제 (음수 가능)
- 플로이드-워셜 알고리즘 : 전체 쌍 최단 경로 문제

### 다익스트라 알고리즘
- `가중 그래프 G와 간선, 시작점 s가 주어졌을 때, 시작점으로부터 그래프의 임의의 정점까지 최단거리를 구해주는 알고리즘이다.`
- `음이 아닌 가중치를 갖는 무작위 유향 그래프에서의 단일소스 최단 경로 알고리즘 중 점근적으로 가장 빠른 알고리즘이다.`

__알고리즘 방법__
<image src="./image/Dijkstra_Animation.gif">
경로를 계획하고 있을 때, 사실은 위에서 했던 것처럼 도착점이 "방문"한 상태가 될 때까지 기다릴 필요가 없다: 도착점이 "미방문" 꼭짓점들 중 가장 시험적 거리가 작아지면 (그리고 다음 "현재 위치"로 선택될 수 있다면) 알고리즘을 종료할 수 있다.
---
1. 출발 노드와, 도착 노드를 설정
2. 알고 있는 모든 거리 값을 부여
3. 출발 노드부터 시작하여, 방문하지 않은 인접 노드를 방문, 거리를 계산한 다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
4. 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거한다.
5. 도착 노드가 미방문 노드 집합에서 벗어나면, 알고리즘을 종료한다.


__의사 코드 (psuedo code)__
```
function Dijkstra(Graph, source):
    dist[source] ← 0                           // 초기화

    create vertex set Q

    for each vertex v in Graph:
        if v ≠ source
            dist[v] ← INFINITY                 // 소스에서 v까지의 아직 모르는 길이
            prev[v] ← UNDEFINED                // v의 이전 노드

        Q.add_with_priority(v, dist[v])


    while Q is not empty:                      // 메인 루프
        u ← Q.extract_min()                    // 간선의 길이가 최저인 item 리턴
        for each neighbor v of u:              // Q에 여전히 남아 있는 v에 대해서만
            alt ← dist[u] + length(u, v)
            if alt < dist[v]
                dist[v] ← alt
                prev[v] ← u
                Q.decrease_priority(v, alt)

     return dist, prev
```
만약 source에서 target까지의 최단 경로만을 구하고 싶다면, 15번째 줄에 u = target을 추가해서 종료시킬 수 있다. 그리고 나서는 source에서 target까지의 최단 경로를 역방향 반복을 통해서 읽을 수 있다:

```
S ← empty sequence
u ← target
while prev[u] is defined:                // 스택 S로 최단 경로를 만든다
    insert u at the beginning of S         // 꼭짓점을 스택에 넣는다
    u ← prev[u]                           // target에서 source로 이동한다
insert u at the beginning of S             // source를 스택에 넣는다
```

__코드구현 (Python)__
```
#Input
# 6 9
# 1 2 7
# 1 3 9
# 1 6 14
# 2 3 10
# 2 4 15
# 3 4 11
# 3 6 2
# 4 5 6
# 5 6 9
import sys

N, M = map(int, input().split(" "))
G = [[0]* (N+1) for _ in range(N+1)]

def pprint(arr):
    for line in arr:
        print(line)

visited = [0 for _ in range(1+N)]

for _ in range(M):
    v1, v2, cost = map(int,sys.stdin.readline().split(" "))    
    G[v1][v2] = cost
    G[v2][v1] = cost

pprint(G)

import heapq as hq

def Dijkstra(Graph, source):    
    queue = []
    
    dist = [float('inf') for _ in range(1+N)]
    dist[source] = 0

    hq.heappush(queue, (dist[source], source))
    
    while queue:
        # print(queue)
        # print(dist)
        cur_dist, cur_dest = hq.heappop(queue)
        if dist[cur_dest] < cur_dist: # 기존에 있는 거리보다 긴 경우
            continue

        for i in range(1, N+1):
            new_dest = i
            new_dist = G[cur_dest][new_dest]
            if new_dist != 0:
                distance = cur_dist + new_dist
                if distance < dist[new_dest]:
                    dist[new_dest] = distance
                    hq.heappush(queue, (distance, new_dest))
    return dist

answer = Dijkstra(G, 1)
print(answer)
```
- 시간복잡도 : O(V**2), 우선순위큐를 사용하는 경우 O(ElogV)

### 벨만-포드 알고리즘
: 어떤 정점 A에서 어떤 정점 B까지의 최단거리는 최대 V-1개의 간선을 사용한다. (=시작 정점 A를 포함하여 최대 V개의 정점을 지난다)

__알고리즘 방법__
1. 시작 정점을 결정한다.
2. 시작 정점부터 다른 정점까지 거리 값 모두 무한대로 초기화 한다.(시작 정점은 0으로 초기화)
3. 현재 정점의 모든 인접 정점들을 탐색하며, 기존에 기록된 인접 정점까지의 거리보다 현재 정점을 거쳐 인접 정점에 도달하는 거리가 더 짧다면 인접 정점까지의 거리를 갱신한다.
4. 3번을 V-1번 반복한다.
5. 위 과정을 모두 마친 후에도 거리가 갱신되는 경우가 있다면 그래프에 음수 사이클이 존재한다는 것을 알 수 있다.


__코드 구현(Python)__
```
def bellman_ford(graph, start):
    distance, predecessor = dict(), dict()  # 거리 값, 각 정점의 이전 정점을 저장할 딕셔너리
    # 거리 값을 모두 무한대로 초기화 / 이전 정점은 None으로 초기화
    for node in graph:  
        distance[node], predecessor[node] = float('inf'), None
    distance[start] = 0  # 시작 정점 거리는 0

    # 간선 개수(V-1)만큼 반복
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:  # 각 정점마다 모든 인접 정점들을 탐색
                # (기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리)인 경우 갱신
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour] = distance[node] + graph[node][neighbour]
                    predecessor[neighbour] = node

    # 음수 사이클 존재 여부 검사 : V-1번 반복 이후에도 갱신할 거리 값이 존재한다면 음수 사이클 존재
    for node in graph:
        for neighbour in graph[node]:
            if distance[neighbour] > distance[node] + graph[node][neighbour]:
                return -1, "그래프에 음수 사이클이 존재합니다."

    return distance, predecessor
```

- 시간복잡도 : O(VE)

### 플로이드 알고리즘 (Floyd) - DP
: 모든 정점 쌍에 대해서 둘 사이의 최단 거리를 구할 수 있다.

### 플로이드 알고리즘 단계
1. 그래프의 초기화
 - 초기에 직접적으로 연결되어 있지 않은 경로는 INF로 설정하고, 자기 자신까지의 비용은 0 으로 만들어준다. 
2. 플로이드 알고리즘 적용
- 시작점을 i, 끝점을 j, 경유점을 k 라고 할때 다음 식 `adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])`를 반복한다.
3. 연결되지 않는 선이 INF로 되어 있기 때문에 min의 값에서 제외가 되고 모든 정점쌍 사이에 최단 거리를 구할 수 있다.

<image src="./images/Floyd.png"/>

### 플로이드 알고리즘 코드
```
# input
# 5 6
# 0 1 2
# 0 2 3
# 1 4 10
# 2 4 4
# 2 3 1
# 3 4 2

import sys
import pprint as pp

V, E = map(int, sys.stdin.readline().split(" "))
W = [[0] * V for _ in range(V)]
D = []
for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split(" "))
    W[v1][v2] = cost
    W[v2][v1] = cost

for i in range(V):
    tmp = []
    for j in range(V):
        if i == j:
            tmp.append(0)
        elif W[i][j] != 0:
            tmp.append(W[i][j])
        else:
            tmp.append(float('inf'))
    D.append(tmp)

#pp.pprint(W)
pp.pprint(D)

for i in range(V):
    for j in range(V):
        for k in range(V):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

pp.pprint(D)
```
- 시간복잡도 : `O(V^3)`
- 공간복잡도 : `O(V^2)`


## 최소스패닝트리(MST)

### 크루스칼 알고리즘

### 프림 알고리즘

