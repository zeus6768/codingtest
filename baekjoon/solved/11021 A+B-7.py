t = int(input())
arr = []
for i in range(t):
    a, b = map(int, input().split())
    arr.append(a + b)

[print("Case #%d: %d" % (j + 1, arr[j])) for j in range(len(arr))]