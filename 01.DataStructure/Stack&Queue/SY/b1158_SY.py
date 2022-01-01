# b1158_SY
answer = []
N, K = map(int, input().split())
list = list(range(1, N+1))
index = -1

for _ in range(N-1):
    index += K
    try:
        answer.append(str(list.pop(index)))
        index -= 1
    except IndexError:
        while 1:
            try:
                answer.append(str(list.pop(index)))
                index -= 1
                break
            except IndexError:
                index -= len(list)

answer.append(str(list[0]))

print("<"+", ".join(answer)+">")
