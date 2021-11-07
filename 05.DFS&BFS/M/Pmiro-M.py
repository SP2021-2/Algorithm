
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temp3+4awhdjh
anfjl
asfahe
"""

from sys import stdin
from collections import deque



def pprint(arr):
    for line in arr:
        print(line)

def bfs(now, n ,m):
    mx = [0, 1, 0, -1]
    my = [1, 0, -1, 0]
    check = 0;
    for i in range(4):
        newX = now[0] + mx[i]
        newY = now[1] + my[i]
        if(newX < n and newY < m):
            if( newX >= 0  and  newY >= 0 and [newX, newY] not in visited and array[newX][newY] == '1' ):
                needVisit.append([newX, newY])
                check += 1
    return check
#m,n = map(int, stdin.readline().split())           
m,n = map(int,input().split())
array = []         
for i in range(n):
    array.append(list(input()))
    #array.append(list(stdin.readline()))
    

visited = deque()
needVisit = deque()

start = [0,0]
needVisit.append(start)
shortNum = 0
check = 1
nextCheck =0
while(True):
    for i in range (check):
        now = needVisit.popleft()
        if(now[0] == n-1 and now[1] == m-1):
            break
        visited.append(now)
        nextCheck += bfs(now , n ,m)
    shortNum += 1
    if(now[0] == n-1 and now[1] == m-1):
            break
    check = nextCheck
    nextCheck = 0
print(shortNum)
