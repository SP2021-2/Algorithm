# 프로그래머스 42748 - k번째 수
# 후기
# - 배열 인덱스 잘 확인하기!

def solution(array, commands):
    
    answer = []
        
    for i in range (0, len(commands), 1) :
        temp = []
        temp = array[commands[i][0]-1 : commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2]-1])
    
    return answer