arr1 = [int(input()) for _ in range(10)]
arr2 = [num % 42 for num in arr1]
arr3 = []
for n in arr2:
    if n in arr3:
        pass
    else:
        arr3.append(n)
print(len(arr3))