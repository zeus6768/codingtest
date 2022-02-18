from sys import stdin
a, b = map(int, stdin.readline().split())
while b:
    a, b = b, a % b
print(a)