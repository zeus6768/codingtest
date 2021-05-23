from sys import stdin
a, b, c = map(int, stdin.readline().split())

# 최대공약수
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

print(GCD(GCD(a, b), c))
