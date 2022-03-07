N = int(input())

def sol(N):
    if N == 1:
        return ["*"]
    
    stars = sol(N//3)
    L = []

    for S in stars:
        L.append(S*3)
    for S in stars:
        L.append(S+" "*(N // 3)+S)
    for S in stars:
        L.append(S*3)
    return L
    

print("\n".join(sol(N)))