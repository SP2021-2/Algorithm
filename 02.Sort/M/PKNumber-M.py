def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        newArr = array[commands[i][0]-1:commands[i][1]]
        newArr.sort()
        print(newArr) 
        answer.append(newArr[commands[i][2]-1])
    return answer

