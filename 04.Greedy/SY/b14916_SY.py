# b14916
n = int(input())

coin = n // 5
if n % 5 == 0 :
    print(coin)
else :
    if n % 5 % 2 == 0 :
        coin += n % 5 // 2
        print(coin)
    elif coin == 0 :
        print(-1)  
    else :
        coin += (n % 5 + 5) // 2 - 1
        print(coin)

    
