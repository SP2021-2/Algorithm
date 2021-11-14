from sys import stdin
n = int(input())
array = []
for i in range(n):
    word = (stdin.readline())
    if(word not in array):
        array.append(word)


for i in range(len(array)-1):
    for j in range (i+1, len(array)):
        if(len(array[i]) > len(array[j])):
            array[i], array[j] = array[j], array[i]
        elif(len(array[i]) == len(array[j])):
            if(array[i] > array[j]):
                 array[i], array[j] = array[j], array[i]
        
for i in range(len(array)):
    print(array[i])

