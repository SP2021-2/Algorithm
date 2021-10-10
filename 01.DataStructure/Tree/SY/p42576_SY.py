# p42576_SY
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    length = len(participant)
    for i in range(length-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == "":
        answer = participant[-1]
    return answer
