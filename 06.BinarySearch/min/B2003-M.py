num , need = map(int, input().split())
arr = list(map(int, input().split()))
#sys.stdin.readline().strip()
i = 0
j = 0
check = 0;
sum = 0
while i <= len(arr):
    
    if(i != len(arr)):
        if sum < need:
            sum += arr[i]
            i += 1
        
        elif sum > need:
            sum -= arr[j]
            j += 1
     
    else :
        if sum > need:
            sum -= arr[j]
            j += 1
        else: 
            i += 1
     
    if sum == need:
        check += 1
        sum -= arr[j]
        j += 1
   
    #print("i", i)
    #print("j" ,j)
    #print("check" , check)
    #print("sum",sum)   
        

print (check)
