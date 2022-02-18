arr = []

n = int(input())
[arr.append(int(input())) for _ in range(n)]

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

[print(k) for k in arr]