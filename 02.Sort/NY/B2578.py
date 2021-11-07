# 백준 2578 - 빙고
import sys

line = 0
chulsuArr = []

for i in range (5) :
    N = list(map(int, sys.stdin.readline().split()))
    chulsuArr.append(N)

mcArr = ""

for i in range (5) :
    M = input()
    mcArr += (M + " ")

mcArr = mcArr.split()

def drawLine (arr, line) :
    for i in range (len(arr)) :
        if arr[i] == [0, 0, 0, 0, 0] :
            line += 1

    count = 0
    for i in range (len(arr)) :
        for j in range (len(arr)) :
            if arr[j][i] == 0 :
                count += 1
        if count == 5 :
            line += 1
            count = 0
    
    count = 0
    for i in range (len(arr)) :
        if arr[i][i] == 0 :
            count += 1
        if count == 5 :
            line += 1
            count = 0

    for i in range (len(arr)-1, 0, -1) :
        if arr[i][i] == 0 :
            count += 1
    if count == 5 :
            line += 1
            count = 0

    return line

k = 0

while (k < 25) :
    
    if k >= 11 :
        result = drawLine(chulsuArr, line)
        if result >= 3 :
            print(result);
            break;

    for i in range (len(chulsuArr)) :
        for j in range (len(chulsuArr)) :
            if (mcArr[k] == chulsuArr[i][j]) :
                chulsuArr[i][j] = 0
                break
    
    print(chulsuArr)

    k += 1
    