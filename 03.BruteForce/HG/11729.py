N = int(input())

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end)
    print(start, end)
    hanoi_tower(n-1, 6-start-end, end)

print(2**N-1)
hanoi_tower(N, 1, 3)
