def solution(board, moves):
    check = []
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if(board[j][moves[i]-1] != 0):
                check.append(board[j][moves[i]-1])
                if(len(check) >= 2):
                    if(check[-2] == check[-1]):
                        answer += 2
                        check.pop(-1)
                        check.pop(-1)
                board[j][moves[i]-1] = 0
                break
                
    #다시 나가~
    return answer
