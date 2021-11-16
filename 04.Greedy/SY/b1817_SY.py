# b1817
import sys
n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))
box = 0
if n != 0 :
    box = 1
    weigt = 0
    for b in books :
        weigt += b
        if weigt > m :
            box += 1
            weigt = b
print(box)

