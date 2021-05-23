import sys
sys.setrecursionlimit(10000)

def tri(n):
    if n <= 2:
        return 0
    elif n % 2:
        d = (n + 1) // 4
        return tri(n - 3) + d
    else:
        return tri(n - 3)

n = int(sys.stdin.readline())
print(tri(n))