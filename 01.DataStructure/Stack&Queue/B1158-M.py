num,jump = (input ().split())
num = int(num)
jump = int(jump)
arr = list(range(1,num+1))
print_arr =[]
pointer =jump-1

while(len(arr) != 0):
    print_arr.append(arr[pointer])
    arr.pop(pointer)
    if(len(arr)==0):
        break
    pointer += jump-1
    while(pointer > len(arr)-1):
        pointer -= len(arr)
        
print("<",end ="")
for i in range(len(print_arr)):
    if(i == len(print_arr)-1):
       print(print_arr[i],end="")
    else:
       print(print_arr[i],end=", ")
print(">",end ="")       
    
    
