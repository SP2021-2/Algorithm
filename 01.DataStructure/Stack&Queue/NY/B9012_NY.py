#백준 - 9012 ok
#2. 9. 00. 프로그래머스

t = int(input())

for i in range(t) :
    str = input()
    q = []
    score = 0

    for s in range(0, len(str)) :
        if str[s] == "(" :
            q.append(str[s])
        elif str[s] == ")" :
            try :
                q.pop()
            except IndexError :
                print("NO")
                score += 1
                break
    if len(q) != 0 :
        print("NO")
        score += 1
    elif score == 0 :
        print("YES")
    
        

