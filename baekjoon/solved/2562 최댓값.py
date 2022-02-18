arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
mx = max(arr)
num = arr.index(mx) + 1
print(f"{mx}\n{num}")