#프로그래머스 - 해시 42576 해시로 안 함... ㅠㅠ

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)) :
        try :
            if participant[i] != completion[i] :
                answer = participant[i]
                break
        except(IndexError) :
            answer = participant[i]

    return answer