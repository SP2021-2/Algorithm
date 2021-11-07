#백준 2178 - 미로 탐색

from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range (N) :
    maze.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y) :
    dQueue = deque()
    dQueue.append((x, y))


    while dQueue :
        x, y = dQueue.popleft()

        for i in range (4) :
            ax = x + dx[i]
            ay = y + dy[i]

            if (0 <= ax < N) & (0 <= ay < M) :
                if maze[ax][ay] == 1 :
                    maze[ax][ay] = maze[x][y] + 1
                    dQueue.append((ax, ay))

    return maze[N-1][M-1]


print(BFS(0, 0))