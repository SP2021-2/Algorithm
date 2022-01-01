#p42748_SY
def solution(array, commands):
    answer = []
    for l in range(len(commands)) :
        i, j, k = commands[l][0] - 1, commands[l][1] - 1, commands[l][2] - 1
        arr = sorted(array[i:j+1])
        answer.append(arr[k])
    return answer