# 그래프 (Graph)
Algorithm Study


## 플로이드 알고리즘 (Floyd) - DP
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

# pp.pprint(W)
pp.pprint(D)

for i in range(V):
    for j in range(V):
        for k in range(V):
            D[i][j] = min(D[i][j], D[i][k]+D[k][j])

pp.pprint(D)

```

- 시간복잡도 : `O(n^3)`
- 공간복잡도 : `O(n^2)`

### 외판원 문제(The Travleing sales-woman problem) - DP
: 외판원이 거주하고 있는 도시에서 출발하여 각 도시를 한 번씩 방문하고, 다시 출발한 도시로 돌아오는 가장 짧은 여행길을 찾고 싶다. 이런 최단 여행 경로를 구하는 문제를 외판원 문제라고 한다.

