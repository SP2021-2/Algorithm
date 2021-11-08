# Algorithm
Algorithm Study

# 이번주 문제
---
- [DFS와 BFS](https://www.acmicpc.net/problem/1260)
- [미로탐색](https://www.acmicpc.net/problem/2178)
- [토마토](https://www.acmicpc.net/problem/7576)
---
- [거스름돈](https://www.acmicpc.net/problem/14916)
- [짐 챙기는 숌](https://www.acmicpc.net/problem/1817)
- [조이스틱](https://programmers.co.kr/learn/courses/30/lessons/42860)
```
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

def pprint(arr):
    for line in arr:
        print(line)

def bfs():
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]
    # 
    return cnt
mage = []
for _ in range(N):
    mage.append(list(map(int, list(sys.stdin.readline().rstrip()))))
print(bfs())
```
## 리뷰 작성 방식
1. 코드관련 리뷰는 __Commits__ 에 작성합니다.
2. 기타 리뷰는 __Conversation__ 에 작성합니다.
2. 모든 문제에 리뷰를 1줄 이상 작성합니다.

[문제링크](https://github.com/tony9402/baekjoon)
## PR 방식
1. git checkout main (메인 브랜치로 이동)
2. git pull (깃헙 원격 저장소와 업데이트)
3. git checkout -b 브랜치이름 (새로운 브랜치 생성!)
4. git add (여러 파일 혹은 ./*)
5. git commit -m (커밋이름)
6. git push origin (브랜치이름)
7. 깃 저장소의 Pull requests 탭에서 Compare & pull request 클릭
8. 코드 리뷰
9. git branch -D 브랜치 (생성된 로컬 브랜치 삭제)
10. git push origin --delete 브랜치 (생성된 원격 브랜치 삭제)

> 백준은 B문제번호, 프로그래머스는 P문제번호로 commit 할 것
