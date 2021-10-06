# 백준 - 1158
import sys

num, k = map(int, sys.stdin.readline().split())
circleQ = []
arr = []
removeIndex = k - 1

#1~n까지 삽입하기
for n in range(num) :
    circleQ.append(n+1)


while len(circleQ) > 0 :

    if len(circleQ) < k :
        removeIndex = k % len(circleQ) - 1
        arr.append(circleQ.pop(removeIndex))
        for i in range (0, removeIndex, 1) :
            circleQ.append(circleQ.pop(0))

    else :
        arr.append(circleQ.pop(removeIndex))
        for i in range (0, removeIndex, 1) :
            circleQ.append(circleQ.pop(0))

result = ""
for i in range (len(arr)) :
    if i == len(arr) - 1:
        result += str(arr[i])
    else :
        result += str(arr[i]) + ", "

print("<%s>" %result)
