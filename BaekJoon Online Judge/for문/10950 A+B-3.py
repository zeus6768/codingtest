arr = []
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    arr.append(a + b)
[print(j) for j in arr]