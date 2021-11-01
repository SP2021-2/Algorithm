# 프로그래머스 - 64061 ok

def solution(board, moves):
    answer = 0

    stacks = []
    bucket = []
    
    for i in range (len(board)) :
        tmp = []
        for j in range(len(board[0])) :
            if board[j][i] != 0 :
                tmp.append(board[j][i])
        tmp.reverse()
        stacks.append(tmp)    
    
    for m in range (len(moves)) :
        try :
            bucket.append(stacks[moves[m]-1].pop())
        except IndexError :
            continue
    
    for q in range (len(bucket)) :
        for b in range (len(bucket)) :
            if b < len(bucket) - 1 :
                if bucket[b] == bucket[b+1] :
                    bucket.pop(b)
                    bucket.pop(b)
                    answer += 2

    return answer