n = input()
arr = list(map(int, input().split()))
sorted_arr = sorted(arr, reverse=True)
[print(num, end = ' ') for num in sorted_arr]