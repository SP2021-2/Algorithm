# 완전 탐색(BruteForce)
완전 탐색(BruteForce)은 컴퓨터의 빠른 계산 능력을 이용해 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법을 의미한다. 가능한 방법을 전부 만들어 보는 알고리즘을 뜻하며, 직관적이고 이해하기 쉬워 문제의 정확한 결과값을 얻어낼 수 있는 가장 확실하며 기초적인 방법이다. 

## 완전탐색 기법을 활용하는 방법
1) 해결하고자 하는 문제의 가능한 경우의 수를 대략적으로 계산한다.
2) 가능한 모든 방법을 다 고려한다.
3) 실제 답을 구할 수 있는지 적용한다.

## 완전탐색 기법
1. 반복 / 조건문을 활용해 모두 테스트 하는 방법
2. 순열(Permutation) - n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
3. 재귀 호출
4. 비트마스크 - 2진수 표현 기법을 활용하는 방법
5. BFS, DFS를 활용하는 방법

### 순열과 조합
- 순열(Permutation) : n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
- 조합(Combination) : n개의 원소 중 r개의 원소를 순서에 상관없이 선택하는 방법

__python에서의 순열,조합 사용방법__
library itertools
- 소스코드
```
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```
```
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
```

```
import itertools as it
arr = [1,2,3,4,5]
string = 'ABCD'

it.permutations(arr)
it.permutations(string, 2)

it.combinations(arr, 3)
it.combinations(string, 2)
```
## DFS / BFS
### 깊이 우선 탐색 (DFS, Depth First Search)

한 경로로 탐색하다 특정 상황에서 최대한 깊숙하게 들어가서 확인 후 다시 돌아가 다른 경로로 탐색하는 방식.

BFS와의 큰 차이점은 DFS는 탐색을 한 뒤 이전의 정점으로 돌아온다는 것이다. 이것을 백트래킹이라고 한다.

그래프 알고리즘에서 기초가 되는 탐색 방식으로 반드시 숙지가 필요하다.

DFS 활용 : 백트래킹(경우의 수), 단절선 찾기, 단절점 찾기, 위상정렬, 사이클 찾기 등.

__DFS 순서__
> 1. 체크 인
> 2. 목적지에 도착했는가?
> 3. 연결된 곳을 순회
> 4. 갈 수 있는 가?
> 5. 간다.
> 6. 체크아웃, 돌아온 체크를 아웃.

- 재귀 용법
```
visited = []

def dfs(v):
    if isGoal:
        return
    visited[v] = True # visited.append(v)
    
    for i in G[v]:
        if not visited[v]:
            DFS(i)

    visited[v] = False
```
- 스택 이용
```
def dfs(v):
    st = []
    st.append(v)

    while st:
        cur = st.pop()
        if isGoal:
            break
        visited[cur] = True
        for v in G[cur]:
            if not visited[v]:
                st.append(v)
```
### 너비 우선 탐색 (BFS, Breath First Search)

시작 노드에서 시작하여 인접한 노드를 먼저 탐색하는 방식. 트리구조에서는 계층 순회를 시작하고 각 계층의 모든 노드를 탐색한 뒤 그 아래 계층으로 넘어간다 . 일반적으로 Queue 자료구조를 이용하여 구현. 
        
BFS 활용 : 최단 경로 찾기, 위상정렬 등.
* BFS로 최단 경로 문제를 해결 가능한 것은 가중치가 1일때 만이다. 1이 아니라면 다익스트라 혹은 벨만 포드 알고리즘을 같이 응용하여 사용해야한다.

__BFS 순서__
> 1. 큐에서 꺼내옴
> 2. 목적지에 도달했는가?
> 3. 연결된 곳을 순회
> 4. 갈 수 있는가?
> 5. 체크인 & 큐에 넣음(간다)
> 6. 체크아웃 (일반적으로 사용 X) 
> -> 한번 방문한 곳은 다시 들어가지 않기 때문에 체크아웃 하지 않아도 됨.

```
from collections import deque
# deque를 사용하는 이유는 list.pop(0)를 하게되면 O(n)의 시간복잡도를 갖는다.

def bfs(G, s):
    q = deque()

    while q:
        cur = q.popleft()
        if isGoal:
            return
        for v in G[cur]:
            if canGo:
                visited[v] = True
                q.append(v)
```