import sys

num , need = map(int, input().split())
arr = list(map(int, input().split()))
#sys.stdin.readline().strip()

high = max(arr)
low = 1


def cutTree(mid):
    sum = 0
    for i in arr:
        if(mid < i):
            sum += i - mid
    return sum

check = 0
while low <= high:
    #print("high, low : " , high ,",",low)
    mid = (high + low)//2
    #print("mid : " , mid)
    sum = cutTree(mid)
    #print("sum : ",sum)
    if sum >= need:
        low = mid + 1 
    elif sum < need:
        high = mid - 1
      
print(high)
