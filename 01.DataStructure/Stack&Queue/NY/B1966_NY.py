#백준 - 1966
import sys

repeat = int(input())

for r in range (repeat) :
    num, wonder = map(int, sys.stdin.readline().split())
    tmpList = list(map(int, sys.stdin.readline().split()))
    docs = []
    priority = []
    printNum = 0
    big = 0

    for n in range(len(tmpList)) :
        docs.append([tmpList[n], n])
        priority.append(tmpList[n])

    for i in range (len(priority)) :
        for j in range (len(priority) - 1, i, -1) :
            if  priority[j-1] < priority[j] : 
                tmp = priority[j]
                priority[j] = priority[j-1]
                priority[j-1] = tmp


    while len(docs) != 0 :

        if docs[0][0] == priority[0] :
            printNum += 1
            if docs[0][1] == wonder :
                print(printNum)
                break
            docs.pop(0)
            priority.pop(0)
        else :
            docs.append(docs.pop(0))