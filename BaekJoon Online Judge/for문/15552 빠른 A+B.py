from sys import stdin
arr = []
t = int(stdin.readline())
for i in range(t):
    a, b = map(int, stdin.readline().split())
    arr.append(a + b)
[print(j) for j in arr]