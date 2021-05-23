t = int(input())
arr = []
for i in range(t):
    a, b = map(int, input().split())
    c = a + b
    arr.append([a, b, c])

for j in range(t):
    print("Case #%d: %d + %d = %d" % (j + 1, arr[j][0], arr[j][1], arr[j][2]))