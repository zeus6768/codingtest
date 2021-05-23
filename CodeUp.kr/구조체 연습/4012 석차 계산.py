n = int(input())
array = list(map(int, input().split()))
new_array = sorted(array, reverse = True)
[print(i, new_array.index(i) + 1) for i in array]