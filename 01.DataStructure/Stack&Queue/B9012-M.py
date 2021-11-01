num = 0
num = (int)(input ())
for i in range(num):
    check = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    checkingP = check[1]
    popNum = 0
    while(True):
        existPop = False
        #맨 처음 값의 중요도와 뒤의 중요도 비교 for문
        for j in range(len(arr)-1):
            if(arr[0] >= arr[j+1]):
                continue
            else:
                arr.append(arr[0])
                arr.pop(0)
                checkingP -= 1
                if(checkingP < 0):
                    checkingP = len(arr)-1
                existPop = True
                break
            
        if(not existPop):
            arr.pop(0)
            popNum += 1
            if(checkingP == 0):
                print(popNum)
                break
            else:
                checkingP -= 1
        
    
    

