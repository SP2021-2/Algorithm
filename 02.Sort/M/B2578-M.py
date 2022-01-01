array = [list(map(int, input().split())) for i in range(5)]
check = [list(map(int, input().split())) for i in range(5)]

def checkBingo(arr):
    bingoNum = 0
    rightSlide = 0
    leftSlide = 0
    
    for i in range(5):
        colZeroNum = 0
        verZeroNum = 0
        
        for j in range(5):
            if(arr[i][j] == 0):
                colZeroNum += 1
            if(arr[j][i] == 0):
                verZeroNum += 1  
            if(i == j and arr[i][j]==0):
                rightSlide += 1
            if((i + j) == 4 and arr[i][j]==0):
                leftSlide += 1
                
        if(colZeroNum == 5):
            bingoNum+=1
        if(verZeroNum == 5):
            bingoNum+=1
    if(leftSlide == 5):
        bingoNum+=1
    if(rightSlide == 5):
        bingoNum+=1
    return bingoNum

def checkArr(num, arr):
    for i in range(5):
        for j in range(5):
            if(arr[i][j] == num):
                arr[i][j] = 0
                bingoNum = checkBingo(arr)
                return bingoNum

for i in range(5):
    for j in range(5):
        bingonum = checkArr(check[i][j], array)
        #print(array)
        if(bingonum >= 3):
            print(i * 5 + j + 1)
            break
    if(bingonum >= 3):
        break

