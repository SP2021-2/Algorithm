# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temp3+4awhdjh
anfjl
asfahe
"""

from sys import stdin

node , line , start =map(int , input().split())
#node  ,line , start = map(int, stdin.readline().split())
array = []

for i in range (node):
    array.append([])
    
for i in range (line):
    key, data =map(int , input().split())
    array[key-1].append(data)
    array[data-1].append(key)

for i in range(len(array)):
    array[i].sort(reverse = True)

#DFS 실행
visited = []
needVisit = []
  
needVisit.append(start)
while(len(needVisit) > 0):
    now = needVisit.pop()
    for i in range(len(array[now-1])):
        if (array[now-1][i] not in visited ):
            needVisit.append(array[now-1][i])
    if now not in visited:
        visited.append(now)
for i in (visited):
    print(i, end =" ")    
print()
#BFS 실행
visited = []
needVisit = []

needVisit.append(start)
while(len(needVisit) > 0):
    now = needVisit.pop()
    for i  in range(len(array[now - 1])-1,-1,-1):
        if(array [now -1][i] not in visited):
            needVisit.insert(0, array [now -1][i])
    if now not in visited:
            visited.append(now)
for i in (visited):
    print(i, end =" ")     
