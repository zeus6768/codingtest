n = int(input())
arr = [int(input()) for i in range(n)]
for i in range(n - 1):
    min_index = i
    for j in range(n - 1 - i):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)