go_table = []
for _ in range(19):
    row = list(map(int, input().split()))
    go_table.append(row)

arr = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x - 1, y - 1])

for j in range(len(arr)):
    dy = arr[j][0]
    dx = arr[j][1]
    for k in range(19):
        go_table[dy][k] = int(not go_table[dy][k])
        go_table[k][dx] = int(not go_table[k][dx])
            
for n in range(19):
    for o in range(19):
        print(go_table[n][o], end = ' ')
    print()