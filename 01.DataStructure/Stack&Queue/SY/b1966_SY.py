# b166_SY
answer = []
time = int(input())
for t in range(time):
    N, M = map(int, input().split())
    arr = [int(x) for x in input().split()]
    key = arr[M]
    result = 1
    while arr:
        if arr[0] == key:
            if arr[0] == max(arr):
                answer.append(result)
                break
            else:
                arr.pop(0)
                result += 1
                continue
        arr.append(arr[0])
        arr.pop(0)

print(answer)
