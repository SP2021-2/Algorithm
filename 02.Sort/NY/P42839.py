# 프로그래머스 42839 - 소수 찾기
# 후기 
# - 정규표현식에 대한 이해가 부족한 것 같다.
# - 2, 10번 케이스에 대해서만 오류가 난다 -> 검색해보니 제곱근과 관련이 있다고 하는데 정확히 이해가 되지 않아 다시 한 번 확인해야 한다. 

from itertools import permutations

def solution(numbers):
    answer = 0
    
    temp = []
    numList = []
    
    for i in range (1, len(numbers)+1) :
        temp = permutations(numbers, i)
        for j in (temp) :
            numList.append(int(''.join(j)))
            
    numList = list(set(numList))
    
    result = 0
            
    for i in range (len(numList)) :
        if (numList[i] == 1 | numList[i] == 0) :
            continue
        else :
            for j in range (1, numList[i]+1) :
                if ( numList[i] % j == 0 ) :
                    result += 1
            if ( result == 2 ) :
                answer += 1
            result = 0
                
    return answer
