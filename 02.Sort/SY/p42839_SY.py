# p42839_SY
import itertools
import math
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False # 소수 X
    return True # 소수 O

def solution(numbers):   
    answer = 0
    nums = []
    tmp = []
    parts = list(numbers)
    length = len(parts)
    for i in range(1, length+1) :
        tmp = itertools.permutations(parts, i)
        for t in (tmp) :
            nums.append(int(''.join(t)))
    nums = list(set(nums))
    for n in nums :
        if not (n == 1 or n == 0) :
            if(is_prime_number(n)) : 
                answer += 1
    return answer
