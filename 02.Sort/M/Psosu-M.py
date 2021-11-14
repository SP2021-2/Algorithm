import itertools

def sosu(num):
    if(num == 1 or num == 0 ):
        return 0
    for i in range(2, int(num/2)+1):
        if(num%i == 0):
            return 0
    return 1
    

def solution(numbers):
    arr = list(numbers)
    arr.sort()
    answer = 0
    answerArr = []
    for i in range(1,len(arr)+1):
        newArr =list(map(''.join, itertools.permutations(arr,i)))
        for j in range(len(newArr)):
            if(sosu(int(newArr[j])) and (newArr[j]) not in answerArr and str(int(newArr[j])) not in answerArr):
                answerArr.append(newArr[j])
        print(answerArr)
    answer = len(answerArr)
    return answer

